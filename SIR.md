# The Susceptible-Infected-Removed (SIR) Model for Disease Spread

When a disease is spreading through a population, the SIR model puts individuals into one of three categories:
1. Susceptible - the individual who has not yet caught the disease
2. Infectious - an individual is sick and may spread the disease to susceptible individuals
3. Removed - sometimes called Recovered - these individuals were previously infectious, and either have recovered and are now immune, or have died.  Either way they can not get the disease again or infect susceptible individuals.

We'll look at a simple SIR model called the Kermack-McKendrick Model.

## Model parameters

There are two parameters in the model:
* `b`: the number of interactions each day that could spread the disease (per individual)
* `k`: the fraction of the infectious population which recovers each day

## Agent-based model

To implement an agent-based model, you might have a class which represents a person, with an internal state which is one of `S`, `I`, or `R`.  You would then simulate a population, where people interact and change state according to the model parameters.

## Differential Equations

In the ODE simulation, you will model time dependent variables: `S, I, R` which represent the total number of individuals in each population (if the total population has `N` individuals, then `S + I + R = N` at all times), as well as `s, i, r`, the fraction of each population in the total population, e.g. `s(t) = S(t) / N` (i.e. `s + i + r = 1` at all times).

If we pass to continuous limits, we can get the following system of differential equations:
1. `ds/dt = -b * s(t) * i(t)`
2. `dr/dt = k * i(t)`
3. `di/dt = b * s(t) * i(t) - k * i(t)`
Equation 1 captures how susceptible people are made sick by infectious people by interacting with parameter `b`.  Equation 2 captures how infectious people enter the removed population at rate `k`.  Equation 3 captures how susceptible people become infected, and infectious people are removed. See [this MAA article](https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model) for some additional details on the derivation.

## Resources

* [The SIR Model of Disease Spread (MAA)](https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease)
* [Kermack-McKendrick Model (Wolfram MathWorld)](https://mathworld.wolfram.com/Kermack-McKendrickModel.html)
* [A SIR model assumption for the spread of COVID-19 in different communities (2020)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7321055/)
