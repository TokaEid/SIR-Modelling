import numpy as np


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
        """This function changes the state of a
        person to newState when called"""
        self.state = newState


def simulateInteractions(people, b, a, c):
    """
    This function loops through each person in people.
    If the person has state I_A (infected, asymptomatic),
    then they will have interactions using the helper
    function simulate_asymptomatic. If the person has state I_S
    they will have interactions using the helper function I_S
    """
    for i in range(people.size):  # Loop through each person in  people
        person = people[i]
        index = i

        if person.state == "R" or person.state == "S":  # Skip interaction if already infected or recovered
            continue

        elif person.state == "I_A":
            simulate_asymptomatic(people, a, b, index)

        else:
            simulate_symptomatic(people, c, b, index)


def simulate_asymptomatic(people, a, b, i):
    """
    This function simulates interactions for
    people who are asymptomatic. If they interact
    with someone who has state S, then that person
    will possibly become infected (prob = a). If that person
    becomes infected, there is a 50% chance they will be asymptomatic
    or
    """

    d = 1-a  # Probability that interaction

    for num in range(b):

        I2 = np.random.choice(np.arange(0, people.size - 1))  # Generate a random index
        secondperson = people[I2]  # index of second person in interaction

        # If that randomly selected index is the same as the current
        if I2 == i or secondperson.state == "R" or secondperson.state == "I_A" or secondperson.state == "I_S":
            continue

        else:
            # There is a prob = a that the person will get infected
            is_infected = np.random.choice(['yes', 'no'], p=[a, d])

            if is_infected == "no":
                continue  # The second person did not become infected

            if is_infected == 'yes':
                symptom_query = np.random.choice(['I_S', 'I_A'])  # Determine if new infected is asymptomatic
                secondperson.changeState(symptom_query)



def simulate_symptomatic(people, c, b, i):
    """
    This function simulates interactions for the
    infected that are asymptomatic. If person i has b interacts
    with a person in people who with state S, then that person
    will possibly become infected (prob = c)
    """
    f = 1-c

    for num in range(b):

        I2 = np.random.choice(np.arange(0, people.size - 1))  # Generate a random index
        secondperson = people[I2]  # index of second person in interaction

        # If that randomly selected index is the same as the current
        if I2 == i or secondperson.state == "R" or secondperson.state == "I_A" or secondperson.state == "I_S":  # If that randomly selected index is the same as the current
            continue

        else:
            # There is a prob = a that the person will get infected
            is_infected = np.random.choice(['yes', 'no'], p=[c, f]) #There is a chance a that the person will get infected

            if is_infected == 'no':
                continue  # The second person did not become infected

            else:
                symptom_query = np.random.choice(['I_A', 'I_S'])  # Determine if new infected is asymptomatic
                secondperson.changeState(symptom_query)  # Second


def simulateRecoveries(people, k):
    """
    This function changes the state of a fraction k
    of people with state I to state R
    """
    for person in people:

        # If a person is infected
        if person.state == "I_A" or person.state == "I_S":
            randValue = np.random.random()

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


def simulateSIR(n, b, k, a, c, t):
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
    people = np.zeros(n, dtype=Person)  # Create a matrix of people with their state

    for i in range(n):
        people[i] = Person()

    # Initialize the matrices S, I, R to keep track of number of people with that state each day
    S = np.zeros(t)
    I_A = np.zeros(t)
    I_S = np.zeros(t)
    R = np.zeros(t)

    # Create patient zero, the first person that is infected
    patient0 = people[0]
    patient0.changeState("I_A")
    people[0] = patient0

    # Collect the counts of each state for each day
    for day in range(t):
        if day == 0:
            S[day] = returnCounts(people, "S")
            I_A[day] = returnCounts(people, "I_A")
            I_S[day] = returnCounts(people, "I_S")
            R[day] = returnCounts(people, "R")
        else:
            simulateInteractions(people, b, a, c)
            simulateRecoveries(people, k)
            S[day] = returnCounts(people, "S")
            I_A[day] = returnCounts(people, "I_A")
            I_S[day] = returnCounts(people, "I_S")
            R[day] = returnCounts(people, "R")

    return S, I_A, I_S, R
