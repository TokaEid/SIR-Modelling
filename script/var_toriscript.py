import matplotlib.pyplot as plt
from sir.varsim_tori import *

def form_plot(n, b, k, a, c, t):
    """
    This function plots the outputs of the S, I, R model

    """
    S, I_A, I_S, R = simulateSIR(n, b, k, a, c, t)
    t_series = range(1, t + 1)
    plt.plot(t_series, S, label='Suspectible')
    plt.plot(t_series, I_A, label='Infected Asymptomatic')
    plt.plot(t_series, I_S, label='Infected Symptomatic')
    plt.plot(t_series, R, label='Removed')
    plt.xlabel('Time')
    plt.ylabel('# of People')
    plt.title(f'Discrete model: a={np.round(a, 2)},c={np.round(c, 2)}')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    n = 3000
    a = [0.5, 0.4, 0.3, 0.2]
    cs = [0.5, 0.6, 0.7, 0.8]
    k = 0.01
    b = 1
    t = 200

    for i in range(len(a)):
        form_plot(n, b, k, a[i], cs[i], t)