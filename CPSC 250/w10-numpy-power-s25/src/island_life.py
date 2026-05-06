import numpy as np
import os
import scipy.special  # Special scientific calculations
import sys
import matplotlib.pyplot as plt


# How far to project into the future
generations = np.arange(0, 500, 1) # and try 800


# based on
# https://www2.nau.edu/lrm22/lessons/predator_prey/predator_prey.html
initial_rabbits = 100  # vs. 1000
initial_foxes = 8
alpha = 0.03 # bunny breeding rate of increase
beta = 0.0005  # bunny die off due to predation
delta = 0.5*beta # foxes breeding (efficiency of turning rabbits into foxes)
gamma = 0.05 # foxes die off rate
carry = 0.00003  # and try 0

# zero rabbit population growth if foxes=alpha/beta (~100)
# zero fox pop. growth if rabbits = gamma/delta (

# Set up arrays to hold our data
rabbits_fwd = np.zeros(generations.shape)
foxes_fwd   = np.zeros(generations.shape)

# Assume know starting point
rabbits_fwd[0] = initial_rabbits
foxes_fwd[0] = initial_foxes

# First order ordinary differential equation calculations
# derivative depends on current values
for ndx in range(1,len(generations)):

    # Forward Euler with known derivative exp(x)
    delta_rabbits = alpha*rabbits_fwd[ndx-1] - beta*rabbits_fwd[ndx-1]*foxes_fwd[ndx-1] - carry*rabbits_fwd[ndx-1]*rabbits_fwd[ndx-1]
    delta_foxes = delta*rabbits_fwd[ndx-1]*foxes_fwd[ndx-1] - gamma*foxes_fwd[ndx-1]
    rabbits_fwd[ndx] = rabbits_fwd[ndx-1] + delta_rabbits
    foxes_fwd[ndx] = foxes_fwd[ndx-1] + delta_foxes

    # Enforce limits to show impact of population bust
    if rabbits_fwd[ndx] < 1.0:
        rabbits_fwd[ndx] = 0
    if foxes_fwd[ndx] < 1.0:
        foxes_fwd[ndx] = 0

fig = plt.figure()
plt.plot(generations, rabbits_fwd, 'go:', label='rabbits (fwd)')
plt.plot(generations, foxes_fwd, 'bx:', label='foxes (fwd)')
plt.xlabel("Generations")
plt.ylabel("Population")
plt.legend()
plt.title(f"Rabbit-Fox Population (first.last.yy)")
fig.savefig(os.path.join("data", "island_life.png"))

plt.show()