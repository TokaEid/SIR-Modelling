import numpy as np 
from numpy.random import randint, rand
import matplotlib.pyplot as plt
import time

from sir.discreteSim_spatial import *
from sir import odeSim_spatial


# Discrete Simulation
"""
General codes to generate plots for Discrete Simulation
"""
# PART 1 PICKING PARAMETER p

# Get k, b from midterm checkpoint 
N = 1000
t = 50
k = 0.3
b = 2
q = round(np.sqrt(1/(np.pi*N)*b),2)
ps = [0.1, 0.3, 0.5, 0.7, 1]

position='Center'
num_initial_infected=30


for p in ps:
    S, I, R = discrete_spatial_simulation(k, q, p=p, t=t, n=N, position=position, num_initial_infected=num_initial_infected)
    plt.plot(I, label=f'p={p}')

plt.xlabel('t')
plt.ylabel('Number of Infected')
plt.title(f'Comparison with Different Step Size p with k={k}, q={q}')
plt.legend()
plt.savefig(f'../doc/final/image/spatialDiscretek{k}q{q}.png')
# plt.show()
# Bawed on above result, p=0.3 is chosen because it has a faster infectious rate and more people are infected

# PART 2: DRAW SIR MODEL
N = 1000
t = 50
k = 0.3
b = 2
q = round(np.sqrt(1/(np.pi*N)*b),2)
p = 0.3
num_initial_infected=30

S, I, R = discrete_spatial_simulation(k, q, p, N, t, position='Random', num_initial_infected=10)
plt.plot(S, label='S')
plt.plot(I, label='I')
plt.plot(R, label='R')

plt.xlabel('t')
plt.ylabel('Number of people')
plt.title(f'SIR Spatial Simulation with k={k}, q={q}, p={p}')
plt.legend()
# plt.show()
plt.savefig(f'../doc/final/image/spatialDiscreteSIR.png')

# PART 3 COMPARE DIFFERENT EPICENTER
k = 0.1
b = 0.05
N = 2000
q = np.sqrt(1/(np.pi*N)*b)

positions = ['Random', 'Center', 'Corner']
for pos in positions:
    S, I, R = discrete_spatial_simulation(k, q, p=0.03, t=50, n=2000, position=pos, num_initial_infected=10)
    plt.plot(I, label=pos)

plt.xlabel('t')
plt.ylabel('Number of Infected')
plt.title('Comparison of Different Initial Epicenters ')
plt.legend()
plt.show()


# ODE Simulation
"""
General code you need to plot from odeSim_spatial:

model = odeSim_spatial(n=100, b=3, k=0.1, p=1, t=500, M=200, initial_position='random')  
# initial_position can be 'center', 'corner', 'random' or None (defaults to 'random')

time, s, i, r = model.solve_pdes()

plt.plot(t, s, label='Suspectible')
plt.plot(t, i, label='Infected')
plt.plot(t, r, label='Removed')

"""
# Explore the effect of p with different combination of b and k in PDE simulation
bkpairs = [(1,0.3),(0.6,0.3)]
ts = [200,300]
ps = [0.6,1,2.5]

for bk_index in range(len(bkpairs)):
    for pval in ps:
        start = time.time()
        model = odeSim_spatial.odeSim_spatial(n=100, b=bkpairs[bk_index][0], k=bkpairs[bk_index][1], p=pval, t=ts[bk_index], M=200, initial_position='random')  
        # initial_position can be 'center', 'corner', 'random' or None (defaults to 'random')
        
        sol = model.solve_pdes()
        
        end = time.time()
        print(end - start) # time elapsed
        print(np.mean(sol.y[model.s_idx],axis=0)[-1]) # Final proportion of susceptible people
        plt.plot(sol.t, np.mean(sol.y[model.s_idx],axis=0), label='Suspectible')
        plt.plot(sol.t, np.mean(sol.y[model.i_idx],axis=0), label='Infected')
        plt.plot(sol.t, np.mean(sol.y[model.r_idx],axis=0), label='Removed')
        plt.legend()
        plt.title(f'PDE simulation: b = {model.b}, k = {model.k}, p = {model.p}\n Final proportion of S: {np.round(np.mean(sol.y[model.s_idx],axis=0)[-1],3)}')
        plt.ylabel('Proportion')
        plt.xlabel('t')
        plt.savefig(f'../doc/checkpoint/spatialPDEb{model.b}k{model.k}p{model.p}.png')
        plt.show()

        start = time.time()
        model = odeSim_spatial.odeSim_spatial(n=100, b=bkpairs[bk_index][0], k=bkpairs[bk_index][1], p=pval, t=ts[bk_index], M=200, initial_position='random')  
        # initial_position can be 'center', 'corner', 'random' or None (defaults to 'random')
        
        sol = model.solve_pdes()

inits = ['random','center','corner']
bkpairs = [(1.5,0.3),(0.6,0.3)]
ts = [150,350]
for bk_index in range(len(bkpairs)):
    for init in inits:
        start = time.time()
        model = odeSim_spatial.odeSim_spatial(n=100, b=bkpairs[bk_index][0], k=bkpairs[bk_index][1], p=0.6, t=ts[bk_index], M=200, initial_position=init)  
        # initial_position can be 'center', 'corner', 'random' or None (defaults to 'random')
        sol = model.solve_pdes()
        
        end = time.time()
        print(end - start) # time elapsed
        print(np.mean(sol.y[model.s_idx],axis=0)[-1]) # Final proportion of susceptible people
        plt.plot(sol.t, np.mean(sol.y[model.s_idx],axis=0), label='Suspectible')
        plt.plot(sol.t, np.mean(sol.y[model.i_idx],axis=0), label='Infected')
        plt.plot(sol.t, np.mean(sol.y[model.r_idx],axis=0), label='Removed')
        plt.legend()
        plt.title(f'PDE simulation: b = {model.b}, k = {model.k}, p = {model.p}\n Final proportion of S: {np.round(np.mean(sol.y[model.s_idx],axis=0)[-1],3)}\nInitialization = {init}')
        plt.ylabel('Proportion')
        plt.xlabel('t')
        plt.savefig(f'../doc/checkpoint/spatialPDEInit{init}_{bk_index}.png')
        plt.show()

