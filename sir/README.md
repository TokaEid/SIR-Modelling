# Project

A large component of this course will be a group project.  In the project you will practice:
1. Working with a small group of people on a shared code base
2. Using a research computing cluster to run code (we'll use the Midway cluster at UChicago)
3. Applying several topics we'll see in this course to simulating a real-world problem

## Default Project - Modeling Disease Spread

In this project, you'll work as a group to model how a new disease spreads throughout a population.  Hopefully, this is something everyone can relate to.

You'll share a repository on GitHub which will contain Python code, scripts for submitting jobs on Midway, and your report.

As we go through this course, we'll cover how to solve the different computational problems in this project, so don't worry if you aren't yet sure how to do something described below.  We'll also provide additional guidance on models and implementations for this project, as well as additional guidance on what should be in the midterm checkpoint and final report.


### Midterm Checkpoint

See [midterm_checkpoint.md](midterm_checkpoint.md) for mode details.

We'll start with the SIR (Susceptible-Infected-Removed) model.  The midterm checkpoint will consist of implementing:
1. A discrete agent-based simulation
2. A continuous / ODE simulation

You'll set up some scripts to run simulations on the Midway compute cluster, run these models with some different parameters, and make a preliminary report on your initial findings.

You will also propose some variations on this theme to run in the final submission.

The midterm checkpoint will be due 11/13 at 12pm (noon) Chicago time.

### Final Submission

For the final submission, each group should add a 2-dimensional spatial component to both the agent-based and continuous models.

In your midterm checkpoint, you should propose several variations of the agent-based or continuous models which you will implement and report on for your final solution.
There should be at least one variation proposed for each member of your group (e.g. so a group of 4 should propose at least 4 variations to implement).

Examples might include:
1. Modeling the use of masks to slow disease spread
2. Modeling the use of quarantine, social distancing, etc.
3. Modeling contagion on a social network (e.g. conspiracy theory)
4. Fitting the SIR model to COVID-19 data
5. Implementing a large-scale/high-performance version of the continuous model
6. Modeling the appearance of a new strain which might re-infect recovered individuals
7. A nice visualization relating to the project

The variations proposed can be governed by interests of group members.  E.g. if one member is interested in Bayesian hierarchical modeling, they might propose using PyStan to fit data.  If one member is interested in PDEs, they might propose improvements to the continuous model.  You might also propose replicating a computational experiment in a a paper related to this topic.  In general, you should propose variations that will be fairly straightforward to implement, since you might start to drift into research territory otherwise.  You do not need to be exhaustive - the point is just to try out a few different ideas.

Again, you will use the Midway compute cluster to explore the behavior of these models.

Your final report should contain a description of the models, the variations/interventions you investigated, and your findings.  The report can be either in PDF form (e.g. generated using LaTeX), or as a web page (something that can be viewed in a web browser), or something like markdown which can be used to generate a PDF or webpage (include instructions on how to generate the final product).  The source for the report should be contained in the project repository.

The final report will be due during finals period.

## Due Dates

* The Midterm checkpoint will be due 2/23 at 1:29pm Chicago time.
* The Final Report will be due during finals week.
