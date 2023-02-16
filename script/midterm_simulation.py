# -*- coding: utf-8 -*-
#from sir import odeSim
from sir.odeSim import odeSim
from sir.discreteSim import simulateSIR
import matplotlib.pyplot as plt
import numpy as np


def Plot_Simulation_ode(model,filename):
    # Plot simulation results for ODE model
    sol = model.solve_odes()
    plt.plot(sol.t, model.n * sol.y[0],label='Suspectible')
    plt.plot(sol.t, model.n * sol.y[1],label='Infected')
    plt.plot(sol.t, model.n * sol.y[2],label='Removed')
    plt.xlabel('Time')
    plt.ylabel('# of People')
    plt.title(f'ODE model: b={np.round(model.b,2)},k={np.round(model.k,2)}')
    plt.legend()
    plt.savefig(filename)
    plt.show()

def Plot_Simulation_discrete(n,b,k,t,filename):
    # Plot simulation results for ODE model
    SS, II, RR = simulateSIR(n,b,k,t)
    t_series = range(1,t+1)
    plt.plot(t_series, SS,label='Suspectible')
    plt.plot(t_series, II,label='Infected')
    plt.plot(t_series, RR,label='Removed')
    plt.xlabel('Time')
    plt.ylabel('# of People')
    plt.title(f'Discrete model: b={np.round(b,2)},k={np.round(k,2)}')
    plt.legend()
    plt.savefig(filename)
    plt.show()


def Get_Final_State_ode(model):
    # Get the final state of S, I, R in a simulation
    sol = model.solve_odes()
    return (sol.y[0][-1], sol.y[1][-1], sol.y[2][-1])

def Get_Final_State_discrete(n,b,k,t):
    # Get the final state of S, I, R in a simulation
    SS, II, RR = simulateSIR(n,b,k,t)
    return (SS[-1]/n, II[-1]/n, RR[-1]/n)


if __name__ == '__main__':
    
    n = 2000
    bs = [0.5,0.5,0.5]
    ks = [0.05,0.3,0.6]
    bs2 = [2,2,2]
    ks2 = [0.3,0.65,0.95]
    t = 200
    t2 = 500
    t3 = 50
    b_series = np.linspace(0,2,50)
    k_series = np.linspace(2,0,50)
    b_series_2 = np.array([int(x) for x in np.linspace(1,6,6)])
    k_series_2 = np.linspace(1,0.1,15)
    
    # Plot the simulation results for different b and k values
    for i in range(len(bs)):
        model_ode = odeSim(n,bs[i],ks[i],t);
        Plot_Simulation_ode(model_ode,f'../doc/checkpoint/ODE_{i}.png');

    # Plot the simulation results for different b and k values
    for i in range(len(bs2)):
        Plot_Simulation_discrete(n,bs2[i],ks2[i],t3,f'../doc/checkpoint/Discrete_{i}.png');
    
    # Plot the phase diagram about the final susceptible number for different b and k values (ode model)
    phase_diagram = np.zeros((k_series.shape[0],b_series.shape[0]))
    for i in range(len(k_series)):
        for j in range(len(b_series)):
            phase_diagram[i][j] = Get_Final_State_ode(odeSim(n,b_series[j],k_series[i],t2))[0];
    
    phasemap = plt.imshow(phase_diagram, cmap='RdYlBu')
    plt.xticks(range(len(b_series))[::10], np.round(b_series[::10],1))
    plt.yticks(range(len(k_series))[::10], np.round(k_series[::10],1))
    plt.xlabel('b (Spread rate)')
    plt.ylabel('k (Recovery rate)')
    plt.title('Phase diagram of final state for ODE model')
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('Proportion of Suspectible People at the end')
    plt.savefig(f'../doc/checkpoint/ode_phase_diagram.png')
    plt.show()
    

    
    # Plot the phase diagram about the final susceptible number for different b and k values (discrete model)
    phase_diagram = np.zeros((k_series_2.shape[0],b_series_2.shape[0]))
    for i in range(len(k_series_2)):
        for j in range(len(b_series_2)):
            phase_diagram[i][j] = Get_Final_State_discrete(n,b_series_2[j],k_series_2[i],t2)[0];
    
    phasemap = plt.imshow(phase_diagram, cmap='RdYlBu',aspect='auto')
    plt.xticks(range(len(b_series_2))[::1], np.round(b_series_2[::1],1))
    plt.yticks(range(len(k_series_2))[::3], np.round(k_series_2[::3],1))
    plt.xlabel('b (Spread rate)')
    plt.ylabel('k (Recovery rate)')
    plt.title('Phase diagram of final state for discrete model')
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('Proportion of Suspectible People at the end')
    plt.savefig(f'../doc/checkpoint/discrete_phase_diagram.png')
    plt.show()

    # plt.show()