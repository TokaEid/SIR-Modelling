import numpy as np
from scipy.spatial import KDTree

class Person(object):
    """
    This class describe all agents in the grid to implement 
    the SIR model with spatial position and movement of agents.
    """
    def __init__(self, p):
        """
        Initiate an agent:
        p: the step of length p in a random direction each individual takes 
            at each time step
        """

        self.pos = np.random.rand(2)
        self.state = 'S'
        self.p = p
    
    def initial_position(self, position):
        """
        Consider different position that the infection started.
        position([pos, pos]): The position
        For infection started from middle, self.pos = (0.5, 0.5)
        For infection started from corner, self.pos = (0, 0)
        """
        self.pos = position

    def get_state(self):
        """
        Getter method: Get the state of the agent
        """
        return self.state

    def set_state(self, new_state):
        """
        Setter method: Set the state of the agent
        """
        self.state = new_state

    def change_state(self):
        if self.get_state() == 'S':
            self.set_state('I')
        elif self.get_state() == 'I':
            self.set_state('R')

    def move(self):
        """
        Change the position of this agent by p
        """
        # Destination position
        dpos = np.random.randn(2)
        dpos = dpos / np.linalg.norm(dpos)

        x = self.pos[0] + dpos[0]*self.p
        y = self.pos[1] + dpos[1]*self.p

        # A successful move
        if 0 <= x <= 1 and 0 <= y <= 1:
            self.pos = (x, y)
        else:
            # remain in the same domain
            self.pos = self.pos


def returnCounts(population, state):
    """
    This function provides the number of people with a particular state 
    Input: 
        State of counts: 'S', 'I', or 'R'
    """
    num = 0
    for person in population:
        if person.state == state:
            num += 1
    return num    

def discrete_spatial_simulation(k, 
                                q, 
                                p, 
                                n, 
                                t, 
                                position='Center', 
                                num_initial_infected=5):
    """
    Input:
    k(float): rate of recovery
    q(float): radius of infection, calculated by b = N * pi * q**2
    p(float): step size for each person
    n(int): the number of population
    t(int): the number of time iteration
    position(str): the start of infection, ['Center', "Corner', 'Random']
    num_initial_infected(int): the number of initial infection

    Return:
        List of S, I, R at time t
    """
    population = [Person(p) for i in range(n)] 

    if position == 'Center':
        pos = np.array([0.5, 0.5])
        for i in range(num_initial_infected):
            population[i].initial_position(pos)
            population[i].change_state()

    elif position == 'Corner':
        pos = np.array([0.0, 0.0])
        for i in range(num_initial_infected):
            population[i].initial_position(pos)
            population[i].change_state()

    elif position == 'Random':
        for i in range(num_initial_infected):
            population[i].change_state()

    S = [returnCounts(population, 'S')]
    I = [returnCounts(population, 'I')]
    R = [returnCounts(population, 'R')]

    for t in range(t):
        position = []
        for p in population:
            p.move()
            position.append(p.pos)
        tree = KDTree(position)
        for i in range(n):
            if population[i].state == 'I':
                inds = tree.query_ball_point(position[i], q)
                for ind in inds:
                    if population[ind].state == 'S':
                        population[ind].change_state()
                if np.random.rand() < k:
                    population[i].change_state()

        S.append(returnCounts(population, 'S'))
        I.append(returnCounts(population, 'I'))
        R.append(returnCounts(population, 'R'))

    return S, I, R
