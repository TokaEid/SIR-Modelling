import numpy as np
from scipy.spatial import KDTree

from sir.discreteSim_spatial import *

# Toka's Variation

class varPerson(Person):
    """
    This class describes a variation of the parent class Person where each individual has more attributes
    associated with social distancing and quarantining
    """
    
    def __init__(self, p=0.03, s=0.5, a=0.4, L=30):
        """
        Initiate an agent:
        p -  the step of length p in a random direction each individual takes 
            at each time step
        s - probability that a Person in the population is practicing social distancing
        a - probability that a Person in the population is quarantining
        L - Number of days the population is on lockdown
        """
        super().__init__(p=0.01)
        
        self.s = s
        self.a = a
        self.L = L
        self.SD = False
        self.Q = False
        self.oldpos = None # Old position
       
    
    def isSocialDist(self):
        """
        A person is social distancing with probability s
        """     
        if np.random.rand() <= self.s:
            
            self.SD = True

            
    def isQuarantined(self):
        """
        A person is quarantining with probability a
        """
        if np.random.rand() <= self.a:
            
            self.Q = True   
            
            
    def moveToQuarantine(self):
        """
        Change the position of this agent to infinity
        where infinity represents a faraway location where they're quarantined
        """
        if self.pos[0] is not np.inf:
            # Only move them to infinity once and store their old position to which they'll return after lockdown ends
            self.oldpos = self.pos
            
        self.pos = [np.inf, np.inf]


        
def runSimulation(k, q, p=0.03, n=1000, t=100, s=0.5, a=0.4, L=30, position='Random', num_initial_infected=10):
    """
    Arguments:
    k -  rate of recovery
    q -  radius of infection
    
    Optional Arguments:
    p - step size (defaults to p = 0.03)
    n - population number (defaults to n = 1000)
    t - the number of time iterations (defaults to t = 100)
    s - probability of social distancing (defaults to s = 0.5)
    a - probability of quarantining (defaults to a = 0.4)
    L - number of days of lockdown (defaults to L = 30)
    position - the start of infection (defaults to position = 'random')
    num_initial_infected - the number of initial infection (defaults to 10)

    Return:
        List of S, I, R at time t
    """
    # Create a population
    pop = [varPerson(p, s, a, L) for i in range(n)] 

    # Initialize position of initially infected people
    if position == 'Center':
        pos = np.array([0.5, 0.5])
        for i in range(num_initial_infected):
            pop[i].initial_position(pos)
            pop[i].change_state()

    elif position == 'Corner':
        pos = np.array([0.0, 0.0])
        for i in range(num_initial_infected):
            pop[i].initial_position(pos)
            pop[i].change_state()

    elif position == 'Random':
        for i in range(num_initial_infected):
            pop[i].change_state()

    # Initialize number of S, I and R people in population
    S = [returnCounts(pop, 'S')]
    I = [returnCounts(pop, 'I')]
    R = [returnCounts(pop, 'R')]

    # Check if each individual is social distancing then check if they're also quarantining
    for p in pop:
        p.isSocialDist()
        # If someone is not social distancing then it's unlikely they're following lockdown protocols either
        if p.SD is True:  
            p.isQuarantined()

    # Start simulation over time t
    for t in range(t):
        
        # Lockdown is for the first self.L days of simulation then lockdown is over
        if t <= p.L:
            lockdown = True
        else:
            lockdown = False
            
        position = []
        counts = []
        counter = 0
        
        # During lockdown, people who are quarantined get moved away from the rest of the population
        # While others move around in random directions
        if lockdown == True:
        
            for p in pop:
                if p.Q is False: # Not quarantined
                    p.move()
                    position.append(p.pos)
                    counter +=1
                
                else:
                    p.moveToQuarantine() # Move to isolation (denoted by infinity)
                    position.append(p.pos)
                    counts.append(counter)
                    counter +=1
            
            # Remove quarantined people from the list of people's locations then form a KDTree
            position = [i for j, i in enumerate(position) if j not in counts] 
            tree = KDTree(position)
        
        # When lockdown is over, quarantined people go back to their old positions and everyone starts moving randomly
        else:
            
            for p in pop:
                
                if p.oldpos is not None:
                    p.pos = p.oldpos
                    
                p.move()
                position.append(p.pos)
                
            tree = KDTree(position)
        
        for i in range(n):
            
            if pop[i].state == 'I': 
                
                if pop[i].Q is True: # If infected person is quarantined, they don't infect anyone else
                    pass
                elif pop[i].SD is True:  # If infected person is social distancing, they don't infect anyone else
                    pass
                else:
                    inds = tree.query_ball_point(position[i], q)
                    for ind in inds:
                        if pop[ind].state == 'S':
                            
                            if pop[ind].SD is True: # If the neighbor of the infected person is social distancing then they aren't infected
                                pass
                            else:
                                pop[ind].change_state()
                
                # Infected person recovers with probability k
                if np.random.rand() < k:
                    pop[i].change_state()
   
                    
        S.append(returnCounts(pop, 'S'))
        I.append(returnCounts(pop, 'I'))
        R.append(returnCounts(pop, 'R'))

    return S, I, R
