# Midterm Checkpoint

The midterm checkpoint will be due 2/23 at 11:59pm (midnight) Chicago time.

For the midterm checkpoint, you should do the following:
1. Read about the SIR model of disease spread - you can find information in [SIR.md](SIR.md).
2. Implement Python code to run simulations of the SIR model (see below), and write a preliminary report
3. Propose several variations or improvements to the SIR model for the final project.  See the  [README](README.md) for some example ideas, but you can be creative and follow your interests.

## Directory Structure

All the code and written materials should be contained in a single GitHub repository, along with instructions for how to run your code and build any written materials.

Create a directory `sir` - this directory should be a Python package, and include class and function definitions.  You should be able to `import sir` from Python to load this package. The package can include subpackages and submodules.

Create a directory `test`, which will include unit tests.

Create a directory `scripts` - this directory should include any scripts used to run code

Create a directory `doc` - this directory should include subfolders `doc/checkpoint` and `doc/final` for the checkpoint and final writeup respectively.


## Implementation

You should implement two types of simulation:
1. A discrete agent-based simulation
2. A continuous / ODE-based simulation

The discrete simulation should be implemented using a class which can be used to create individuals, individuals should have an internal state which represents whether that individual is susceptible, infected, or removed.  The class should provide methods to determine the state of the individual, and change the state of the individual.

In the ODE simulation, you will model time dependent variables: `S, I, R` which represent the total number of individuals in each population (if the total population has `N` individuals, then `S + I + R = N` at all times), as well as `s, i, r`, the fraction of each population in the total population, e.g. `s(t) = S(t) / N` (i.e. `s + i + r = 1` at all times).

Implement unit tests in a `test` folder.  These should include tests to verify that your class methods do what you think they do, and that your ODE simulation satisfies the equations above for some choices of parameter.  Set up these tests to run automatically when changes are pushed to GitHub.

## Simulations

Because we're investigating how a new disease spreads, you can start with a small number of infectious individuals (e.g. 0.1% of the population) for both the continuous and discrete simulations, with the remainder of the population in the susceptible category.

Your simulations should produces some plots of how `s`, `i`, and `r` change over the length of the simulation for a couple different choices of `k` and `b`.

You should also investigate the qualitative behavior of the simulations based on the parameters `b` and `k` in a phase diagram.  For instance, how does the total percentage of the population infected at some point in the simulation depend on these parameters?  Are there parameter regimes where `i` quickly goes to 0?  Are there parameter regimes where everyone is eventually infected?

How well do the discrete and ODE simulations agree?

## Report

In addition to the code you will write, you should prepare a preliminary report.  This can either be a PDF or a file which can be viewed in a web browser.  Put your report in the `doc/checkpoint` folder in the repository, which should contain any files and figures, as well as instructions to generate the PDF or html files (if they are generated from LaTeX, Markdown, etc.)

Your report should have 4 sections.
1. A brief introduction to the SIR model, and notation you will use.  You can use [`SIR.md`](SIR.md), as well as other resources (cite any other resources that contribute to your discussion).
2. A brief description of how you are structuring the Python package `sir`.
3. Report on your preliminary investigations using the agent-based and continuous models.
4. Your proposed variations/improvements for the final project.

Sections 1 should not be very long.  Section 2 should be very brief (about 1 paragraph). Section 3 should include several figures, including:
1. Phase diagrams for the discrete and ODE simulations
2. Example plots of the S,I, and R populations over time for some choices of parameter `b` and `k`.
.  

Section 4 should include 1 proposed variation for each member of the group (e.g. a group of 3 should propose 3 variations).  See the [README](README.md) for some examples.  You should have subsections for each proposed variation which include the following information:
1. What questions you want to answer in the final report, and how you would try to answer these questions using simulations.
2. Any changes to the model in the variation
3. If you are using data, where you will obtain the data
4. If your variation uses a model or idea from a paper or website, include any references

Your report should have a list of references - likely some for your background on the SIR model, and some for your proposed variations.

If you have specific questions for the course staff, please also list them for each model.

## Evaluation

90% of the checkpoint grade will be shared by members of your teams.  This will consist of:
* 40% code (quality, correctness, etc.)
* 50% preliminary report

10% of the checkpoint grade will be based on teammate evaluations.  These evaluations will be kept confidential.  If you believe your score to be unfair, you can reach out to the instruction staff.  We will look at git logs/history if we need to resolve any disputes.  If you do not participate at all, we reserve the right to remove you from the team.
