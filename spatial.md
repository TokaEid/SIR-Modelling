# Spatial Modeling

For your final submission, you should add a (2-dimensional) spatial component to your simulations

In both these problems, the population will be confined to the square `[0,1] x [0,1]`

## Agent-based model

In the original SIR model, individuals had a state (`S`, `I`, or `R`), and interacted with `b` random other individuals at each time step, and at each time step infected individuals had a recovery probability of `k`.

Now, in addition to their disease state, each agent will also have a position given by `pos = (x,y)`, where `0 <= x <= 1` and `0 <= y <= 1`.  You can store this a numpy array of length 2.  We'll also introduce two new variables: `p` and `q`.  Here are the alterations to the simulation:
1. When initializing an individual, you can initialize `pos` uniformly at random (e.g. using `np.random.rand`)
2. At each time step, each individual takes a step of length `p` in a random direction.  If the individual would step outside the domain, they can remain in the same location.  You can sample a random 2-dimensional direction using
```python
dpos = np.random.randn(2)
dpos = dpos / np.linalg.norm(dp)
```
and then scale by `p`.
3. After an individual takes the random step, they interact with all other individuals within radius `q`.  Note that you can use a `KDTree` for this.

While you should keep the parameter `k`, the parameter `b` is no longer necessary, because `q` governs interactions.  Note there is a rough equivalence in expectation `b = N * pi * q**2`, where `N` is the population size (although the spatial component affects disease spread as well).

Use your results from the midterm checkpoint to choose `b` and `k` near the phase transition boundary.  Set `q` from `b` using the above relation, and explore the following questions, starting with a small number of infected individuals:
1. If infected individuals start at the center of the square, how does the total number of individuals infected throughout the simulation change with the parameter `p`?
2. Choose an interesting parameter of `p` using question 1.  How does the simulation qualitatively differ when the initial infected individuals start in a single corner of the square vs. the center of the square vs. being randomly spread out?

## PDE model

Now, we'll update the ODE model to be a PDE.  Like the agent based model, we'll simulate a population on the unit square.  We'll discretize the square into an `M x M` grid (use `M=200` by default, but you can experiment with different sizes).  We can represent the population at each time with three `M x M` arrays, `s(x, t)`, `i(x, t)`, and `r(x, t)`, where `x = (i,j)` is the index on the `M x M` grid.  The random walk for the agent based model becomes diffusion in the continuous limit, so we have a system of PDEs:

1. `\partial s(x, t)/ \partial t = -b * s(x, t) * i(x, t) + p * L * s(x, t)`
2. `\partial r(x, t)/ \partial t = k * i(x, t) + p * L * r(x, t)`
3. `\partial i(x, t)/ \partial t = b * s(x, t) * i(x, t) - k * i(x, t) + p * L * i(x, t)`

Where `L` is the 2-dimensional Laplacian (remember to weight your second derivatives by `h**2 = 1/M ** 2`).  Note that you can turn this into a system of ODEs by vectorizing the 2-dimensional arrays `s`, `i` and `r`.  In this case, we keep the parameter `b` and don't use the parameter `q` (in the agent based model), but we do use the parameter `p` to weight the diffusion term (note that you can relate this to the parameter `p` in the agent-based model, but you need to make sure you take into account the finite difference step size `1/M` - you do not need to derive this in your report).

Again, choose `b` and `k` to be near the phase transition boundary, and explore the following questions:
1. If infected individuals start at the center of the square, how does the total number of individuals infected in the simulation change with the parameter `p`?
2. Choose an interesting parameter of `p` using question 1.  How does the simulation qualitatively differ when the initial infected individuals start in a single corner of the square vs. the center of the square vs. being randomly spread out?  You can investigate this by choosing initial conditions for `i(x,0)` appropriately.
