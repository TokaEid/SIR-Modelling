import numpy as np 
import matplotlib.pyplot as plt

from sir.discreteSim_spatial import *
from sir.variation_2 import *

# Toka's Variation:

# Parameters
k = 0.1
b = 1
q = np.sqrt(1/(np.pi*100)*b)
L = [0, 30, 60]
SD = [0.2, 0.5, 0.8]
Q = [0.2, 0.4, 0.7]

# Changing Lockdown Days
fig, axs = plt.subplots(1, len(L), sharey=True, figsize=(12,4))
fig.tight_layout()
i=0
            
for l in L:
    
    S, I, R = runSimulation(k, q, p=0.01, n=1000, t=100, s=0.5, a=0.4, L=l, position='Random', num_initial_infected=10)
    axs[i].plot(S, label='Susceptible')
    axs[i].plot(I, label='Infected')
    axs[i].plot(R, label='Recovered')
    axs[i].set_title('L = ' + str(l))
    i+=1
    
for ax in fig.get_axes():
    ax.set_xlabel('Time (days)', fontsize=14)
    ax.set_ylabel('Number of People', fontsize=14)
    ax.label_outer()    
    
plt.legend()   
fig.suptitle('Effect of Lockdown', y=0.95, fontsize=18)   
filename = "../doc/final/image/" + "var2_Lockdown.png"
plt.tight_layout()
plt.savefig(filename)  
plt.show()


# Changing Social Distancing Probability
fig, axs = plt.subplots(1, len(SD), sharey=True, figsize=(12,4))
i=0
       
for s in SD:
    
    S, I, R = runSimulation(k, q, p=0.01, n=1000, t=100, s=s, a=0.4, L=30, position='Random', num_initial_infected=10)
    axs[i].plot(S, label='Susceptible')
    axs[i].plot(I, label='Infected')
    axs[i].plot(R, label='Recovered')
    axs[i].set_title('SD = ' + str(s))
    i+=1
    
for ax in fig.get_axes():
    ax.set_xlabel('Time (days)', fontsize=14)
    ax.set_ylabel('Number of People', fontsize=14)
    ax.label_outer()    
    
plt.legend()   
fig.suptitle('Effect of the Probability of Social Distancing', y=0.95, fontsize=18)   
filename = "../doc/final/image/" + "var2_SD.png"
plt.tight_layout()
plt.savefig(filename)  
plt.show()


# Changing Quarantining Probability
fig, axs = plt.subplots(1, len(Q), sharey=True, figsize=(12,4))
fig.tight_layout()
i=0
            
for a in Q:
    
    S, I, R = runSimulation(k, q, p=0.01, n=1000, t=100, s=0.5, a=a, L=50, position='Random', num_initial_infected=10)
    axs[i].plot(S, label='Susceptible')
    axs[i].plot(I, label='Infected')
    axs[i].plot(R, label='Recovered')
    axs[i].set_title('Q = ' + str(a))
    i+=1
    
for ax in fig.get_axes():
    ax.set_xlabel('Time (days)', fontsize=14)
    ax.set_ylabel('Number of People', fontsize=14)
    ax.label_outer()    
    
plt.legend()   
fig.suptitle('Effect of the Probability of Quarantining', y=0.95, fontsize=18)   
filename = "../doc/final/image/" + "var2_Q.png"
plt.tight_layout()
plt.savefig(filename)  
plt.show()
