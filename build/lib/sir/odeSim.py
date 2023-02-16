import numpy as np
from scipy.integrate import solve_ivp

# Instructions on how to import this class
# from odeSim import odeSim
# Define parameters/inputs
# s = odeSim(n,b,k,t)
# sol = s.solve_odes()
# plot(sol.t, sol.y[])

def ReachZero(t, y):
    """
    define an event which indicates that the number of infected people have reached zero
    """
    return y[1] - 1e-6

ReachZero.terminal = False # This will not end the simulation
ReachZero.direction = -1


class odeSim():
    """
    A class that solves ordinary differential equations for the SIR model
    
    Arguments:
        n - Number of people in the population
        
    Optional Arguments:
        b - Number of contacts per day that are sufficient to spread the disease (default b = 1/2)
        k - Fraction of the infected group of individuals that will recover during any given day (default k = 1/3)
        t - Amount of time the simulation will run for (default t = 500 days)
    """
    
    def __init__(self, n, b=1/2, k=1/3, t=500):

        # n is the population number
        # b is the number of contacts per day that are sufficient to spread the disease
        # k is the fraction of the infected group that will recover during any given day 
        # t is the amount of time we want to run the simulation for
        
        self.n = n
        self.b = b
        self.k = k
        self.t = t


    def solve_odes(self):
        """
        Defines the initial conditions then solves the initial value problem with our system of odes
        """

        # S is the number of susceptible individuals
        # I is the number of infected individuals
        # R is the number of recovered or deceased individuals

        # s, i, r are the fractions of the population that are susceptible, infected, and recovered, respectively.
        # s = S/n, i = I/n, r = R/n

        # Initial conditions
        # Initial conditions
        i0 = 0.001      # 0.1% of the population
        s0 = 1 - i0          # the whole population is susceptible except those that are infected
        r0 = 0               # no one is recovered yet

        ics = np.array([s0,i0,r0])

        
        # System of ODEs
        # s'(t) = -b * s(t) * i(t)
        # i'(t) = b * s(t) * i(t) - k * i(t)
        # r'(t) = k * i(t)
        
        f = lambda t, y : np.array([
            -self.b * y[0] * y[1],
            self.b * y[0] * y[1] - self.k * y[1],
            self.k * y[1]
        ] )


        # Time interval
        t_eval = np.linspace(0, self.t, self.t*10)
        t_span = (0, self.t)

        
        # Solve the system of ODEs with initial conditions
        sol = solve_ivp(f, t_span, ics, t_eval=t_eval, events=ReachZero)

        return sol
    
