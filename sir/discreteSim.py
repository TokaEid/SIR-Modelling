import numpy as np
from numpy import random

class Person:
    """
    This class sets up each person in the simulation.
    When initialized, a person has the state "S", meaning
    that the person starts as someone who is susceptible to infection 
    """
    def __init__(self):
        """
        The function initializes the person data type.
        Each person starts off with a state S
        """
        self.state = "S"
        
    def state(self):
        """
        Returns the state of an individual
        """
        return self.state

    def changeState(self, newState):
        "This function changes the state of a person to newState when called"
        self.state = newState


def simulateInteractions(people, b):
    """
    This creates random interactions for each person.
    Each person can have b interactions with others.
    If a person with a state S has an interaction with
    a person with a state I, the person's state will change to I
    """
    for i in range(people.size): #Loop through each person in  people
        person = people[i]
        if person.state == "R" or person.state == "S": #Skip interaction if already infected or recovered
            continue
        for num in range(b):
            I2 = random.choice(np.arange(0, people.size-1)) #Generate a random index
            secondperson = people[I2]  # The person
            if I2 == i or secondperson.state == "R": #If that randomly selected index is the same as the current
                continue
            else:
                secondperson.changeState("I") #If either person in the interaction is infected, then they will both be infected
        

def simulateRecoveries(people, k):
    """
    This function changes the state of a fraction k
    of people with state I to state R 
    """
    for person in people:
        if person.state == "I": #If a person is infected 
            randValue = random.random() 
            if randValue <= k:
                person.changeState("R") 


def returnCounts(people, state):
    """
    This function provides the number of people with a particular state 
    """
    num = 0
    for person in people:
        if person.state == state:
            num += 1
    return num


def simulateSIR(n, b, k, t):
    """
    Driver code for the discrete simulation.
    Uses simulaterecoveries and simulateinteractions to model
    how the disease would spread.
    Parameters:
    n is population,
    b is the number of interactions for a single person
    k is the portion of infected individuals who are removed each day, as a decimal
    t is the number of days to simulate
    """
    people = np.zeros(n, dtype=Person) #Create a matrix of people with their state


    for i in range(n):
        people[i] = Person()

    #Initialize the matrices S, I, R to keep track of number of people with that state each day 
    S = np.zeros(t)
    I = np.zeros(t)
    R = np.zeros(t)

    #Create patient zero, the first person that is infected
    patient0 = people[0]
    patient0.changeState("I")
    people[0] = patient0

    #Collect the counts of each state for each day 
    for day in range(t):
        if day == 0:
            S[day] = returnCounts(people, "S")
            I[day] = returnCounts(people, "I")
            R[day] = returnCounts(people, "R")
        else:
            simulateInteractions(people, b)
            simulateRecoveries(people, k)
            S[day] = returnCounts(people, "S")
            I[day] = returnCounts(people, "I")
            R[day] = returnCounts(people, "R")

    return(S, I, R)

