import numpy as np
from scipy.integrate import solve_ivp
import scipy.sparse as sparse


def forward_diff_matrix(n):
    """
    Generates a forward difference matrix to calculate derivatives
    """
    data = []
    i = []
    j = []
    for k in range(n - 1):
        i.append(k)
        j.append(k)
        data.append(-1)

        i.append(k)
        j.append(k+1)
        data.append(1)

    return sparse.coo_matrix((data, (i,j)), shape=(n, n)).tocsr()
    
def laplacian(n):
    """
    Returns two dimensional laplacian
    """ 
    D = forward_diff_matrix(n)
    
    # Diffusion operator (from lecture notebooks)
    DD = -D.T @ D
    
    # Weighting by h**2
    h = 1 / n
    D = D / h**2

    # Applying sparse.kron to get the second derivative in each direction
    D2x = sparse.kron(sparse.eye(n), DD).tocsr()
    D2y = sparse.kron(DD, sparse.eye(n)).tocsr()

    # Laplacian
    L = D2x + D2y
        
    return L


class odeSim_spatial():
    """
    A class that solves ordinary differential equations for the SIR model

    Optional Arguments:
        n - Number of people in the population
        b - Number of contacts per day that are sufficient to spread the disease (default b = 3)
        k - Fraction of the infected group of individuals that will recover during any given day (default k = 0.1)
        p - Weight of the diffusion term (default p = 1)
        t - Amount of time the simulation will run for (default t = 400 days)
        M - Size of the unit square grid where population resides (default M = 200)
        initial_position - Starting position of infected individuals (default = 'random')
        
    """
    
    def __init__(self, n=100, b=3, k=0.1, p=1, t=400, M=200, initial_position=None):
        
        # Storing the class attributes
        self.n = n
        self.b = b
        self.k = k
        self.t = t
        self.p = p
        self.M = M
        
        # Defaulting initial_position to 'random' if no argument given
        if initial_position is None:
            initial_position = 'random'
            
        self.pos = initial_position
        
        # Calculating laplacian from pre-defined function
        self.L = laplacian(self.M)
        
        # Defining ranges of s, i, and r values in the solution y
        self.s_idx = np.arange(self.M * self.M)
        self.i_idx = np.arange(self.M * self.M, 2 * self.M * self.M)
        self.r_idx = np.arange(2 * self.M * self.M, 3 * self.M * self.M)
                

    def initial_conditions(self):
        """
        Returns the flattened arrays s0, i0, and r0 according to the problem's initial conditions
        """
        
        # Initializing arrays
        i0 = np.zeros((self.M,self.M))
        s0 = np.ones((self.M,self.M))
        r0 = np.zeros((self.M,self.M))
        
        # According to the initial_position, the location of the initially infected individuals changes
        if self.pos == 'center':
            
            # Generate random integers in the center of the grid
            i = np.random.randint(self.M*2/5, self.M*3/5, size=int(self.M/4))
            j = np.random.randint(self.M*2/5, self.M*3/5, size=int(self.M/4))
            
            # Stack the arrays to easily access each coordinate
            entries = np.stack((i,j), axis=1) # Each element in entries is [i,j] such that entries[0] = [i[0], j[0]]
            
            for entry in entries:
                # With a probability of 0.1, change elements in i0 and s0 to be infected
                if np.random.random() <= 0.1:
                
                    i0[entry[0], entry[1]] = 0.001  # 0.1% of population
                    s0[entry[0], entry[1]] = 1 - 0.001
            
            
        elif self.pos == 'corner':
            
            # Generate random integers in the corner of the grid
            i = np.random.randint(0, self.M/5, size=int(self.M/4))
            j = np.random.randint(0, self.M/5, size=int(self.M/4))
            
            entries = np.stack((i,j), axis=1)
            
            for entry in entries:
                
                if np.random.random() <= 0.1:
                
                    i0[entry[0], entry[1]] = 0.001 
                    s0[entry[0], entry[1]] = 1 - 0.001

        else: 
            # Generate random integers anywhere on the grid
            i = np.random.randint(0, self.M)
            j = np.random.randint(0, self.M)
                
            i0[i,j] = 0.001
            s0[i,j] = 1 - 0.001
        
        # Flatten all initial condition arrays
        s0 = s0.flatten()
        i0 = i0.flatten()
        r0 = r0.flatten()
            
        return s0, i0, r0
    
    
    def rhs_pdes(self, t, y):
        """
        Function that outputs the right hand sides of the system of pdes as a flattened array of y:
        
        s'(x,t) = -b * s(x,t) * i(x,t) + p * L * s(x,t)
        i'(x,t) = b * s(x,t) * i(x,t) - k * i(x,t) + p * L * i(x,t)
        r'(x,t) = k * i(x,t) + p * L * r(x,t)
        """
        
        s = -self.b * y[self.s_idx] * y[self.i_idx] + self.p * self.L @ y[self.s_idx]
        i = self.b * y[self.s_idx] * y[self.i_idx] - self.k * y[self.i_idx] + self.p * self.L @ y[self.i_idx]
        r = self.k * y[self.i_idx] + self.p * self.L @ y[self.r_idx]
            
        return np.array([s, i, r]).flatten()
        
        
    def solve_pdes(self):
        """
        Solves the initial value problem and returns the solution of s(x,t), i(x,t), and r(x,t)
        """
        
        # Initial conditions array
        s0, i0, r0 = self.initial_conditions()    
        self.ics = np.array([s0, i0, r0]).flatten()
        
        # Time interval
        t_span = (0, self.t)
        t_eval = np.arange(0, self.t, 1)

        # Solution
        sol = solve_ivp(fun=self.rhs_pdes, t_span=t_span, y0=self.ics, t_eval=t_eval, dense_output=True)

        return sol
