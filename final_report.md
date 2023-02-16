# Final Report

The final report will be due during finals week.

For the final report, you should do the following:
1. Add spatial components to your agent-based and ODE models.  See [spatial.md](spatial.md) for instructions.
2. Implement/explore the variations you proposed in your midterm checkpoint.
3. Write a report which will discuss your findings.

You'll use the same repository you used for your midterm checkpoint.  You can modify your code/scripts.  You can also use your midterm checkpoint write-up as a starting point for the final report, so you don't need to re-write the background sections unless you want to (copy it into a new folder).

## Directory Structure

All the code and written materials should be contained in the same GitHub repository you used for your midterm checkpoint, along with instructions for how to run your code and build any written materials.

Create a directory `sir` - this directory should be a Python package, and include class and function definitions.  You should be able to `import sir` from Python to load this package. The package can include subpackages and submodules (e.g. submodules for different variations).

Create a directory `test`, which will include unit tests.

Create a directory `scripts` - this directory should include any scripts used to run code

Create a directory `doc` - this directory should include subfolders `doc/checkpoint` and `doc/final` for the checkpoint and final writeup respectively.


## Report

In addition to the code you will write and simulations you will run, you should prepare a final report, which should be similar in length/format to a conference paper or short journal article.  The purpose of the report is to explain what you investigated, how you investigated your topics (e.g. model/implementation), and why your investigation was interesting (what should a reader take away from your work).

This can either be a PDF or a file which can be viewed in a web browser (please don't just use GitHub to host a notebook or markdown file - generate a static html web page).  Put your report in the `doc/final` folder in the repository, which should contain any files and figures, as well as instructions to generate the PDF or html files (if they are generated from LaTeX, Markdown, etc.) If your extensions include an interactive visualization, find a good way to display this online. The purpose of the report is to explain what you investigated, how you investigated your topics, and why your investigation was interesting.

Your report should the following sections.
0. Abstract (1 paragraph summary)
1. A brief introduction to the SIR model, the notation you will use, and the different variations you investigate.
2. Sections for the basic SIR model (also in midterm checkpoint), the spatial SIR model, and your variations.  Include any relevant implementation details as well as your results and discussion.
3. A conclusion summarizing your results, discussing limitations of your models, and pointing out interesting directions for further investigation
4. A bibliography

Please limit your report to 10 pages (excluding bibliography) with 1-inch margins (these margins allow for a lot of content per page).  You can put additional figures/results in appendices (not counting to 10 page limit) if you would like, but it is perfectly fine to choose one or two figures per experiment that best illustrate your point in the main text.

## Evaluation

90% of the final report grade will be shared by members of your teams.  This will consist of:
* 40% code (quality, correctness, etc.)
* 50% written report

10% of the project grade will be based on teammate evaluations.  These evaluations will be kept confidential.  If you believe your score to be unfair, you can reach out to the instruction staff.  We will look at git logs/history if we need to resolve any disputes.  If you do not participate at all, we reserve the right to remove you from the team.
