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

## Project Guidelines
In this project, you'll work as a group to model how a new disease spreads throughout a population.  Hopefully, this is something everyone can relate to. You'll share a repository on GitHub which will contain Python code, scripts for submitting jobs on Midway, and your report.

The midterm checkpoint will consist of implementing:
1. A discrete agent-based simulation
2. A continuous / ODE simulation

You'll set up some scripts to run simulations on the Midway compute cluster, run these models with some different parameters, and make a preliminary report on your initial findings. You will also propose some variations on this theme to run in the final submission.

For the final submission, each group should add a 2-dimensional spatial component to both the agent-based and continuous models. You should implement and report your proposed variation of the agent-based or continuous model (from the midterm checkpoint) as part of the final submission.

Your final report should contain a description of the models, the variations/interventions you investigated, and your findings. 

