import numpy as np
import os
import scipy.special  # Special scientific calculations
import sys
import matplotlib.pyplot as plt
from given.special_functions import plot_trapezoids

x_lin = np.linspace(1/32, 100, 50)
recip_x_lin = 1/x_lin

fig = plt.figure()
plt.plot(x_lin, recip_x_lin, 'r*:')
plt.xlabel("x")
plt.ylabel("1/x")
plt.title("Reciprocal 1/x - Linear Scale! (first.last.yy)")
fig.savefig(os.path.join("data", "integration_recip.png"))

# Comment out the next two lines to continue
plt.show()
sys.exit(-1)


#####################
# Demo of log range
#####################

x_log = np.logspace(-3, 2, 50)
recip_x_log = 1/x_log

fig = plt.figure()
plt.plot(x_lin, recip_x_lin, 'rx:')
plt.plot(x_log, recip_x_log, 'bo:')
plt.xlabel("x")
plt.ylabel("1/x")
plt.title("Reciprocal 1/x - log range (first.last.yy)")
fig.savefig(os.path.join("data", "integration_recip_log_range.png"))

# Comment out the next two lines to continue
plt.show()
sys.exit(-1)


increment = 0.25
x_lin2 = np.arange(0.25, 5., increment)
recip_x_lin2 = 1/x_lin2
fig = plt.figure()
plt.plot(x_lin2, recip_x_lin2, 'ko:')
plt.xlabel("x")
plt.ylabel("1/x")
plt.title("Reciprocal 1/x - zoom (first.last.yy)")
fig.savefig(os.path.join("data", "integration_recip_zoom.png"))

fig = plt.figure()
x_midpoints, y_midpoints = plot_trapezoids(x_lin2, recip_x_lin2)

area = np.sum(y_midpoints*increment)
plt.xlabel("x")
plt.ylabel("1/x")
plt.title(f"Reciprocal 1/x area under curve for n={len(x_midpoints)} = {area:.5f} (first.last.yy)")
fig.savefig(os.path.join("data", "integration_recip_approx.png"))

# Comment out the next two lines to continue
plt.show()
sys.exit(-1)

########
# Better approximation of interval rectangles
increment = 0.25
n_increments = []
areas = []
for n in np.logspace(1, 4, 20, dtype='int'):
    print(f"n={n}")
    increment = 1/n
    x_lin2 = np.arange(0.25, 5., increment)
    recip_x_lin2 = 1/x_lin2
    x_midpoints = 0.5 * (x_lin2[0:-1] + x_lin2[1:])
    y_midpoints = 0.5 * (recip_x_lin2[0:-1] + recip_x_lin2[1:])
    n_increments.append(n)
    areas.append(np.sum(y_midpoints*increment))


# Theoretical integral of 1/x = log(x)
integral = np.log(5)-np.log(0.25)  # Answer

fig = plt.figure()
plt.plot(n_increments, areas, 'rx:')
plt.plot([n_increments[0], n_increments[-1]], [integral, integral], 'b:')
plt.xlabel("Number of intervals (n)")
plt.ylabel("Integral of 1/x")
plt.title(f"Integral of 1/x from 0.25 to 5 (first.last.yy)")
fig.savefig(os.path.join("data", "integration_recip_integral.png"))

# Comment out the next two lines to continue
plt.show()
sys.exit(-1)

#####################
# Demo of integration example
#####################

########
# Better approximation of interval rectangles
n_increments = []
areas = []
for n in np.logspace(1, 4, 20, dtype='int'):
    print(f"n={n}")
    increment = 1/n
    x_lin2 = np.arange(1, np.exp(1), increment)
    recip_x_lin2 = 1/x_lin2
    x_midpoints = 0.5 * (x_lin2[0:-1] + x_lin2[1:])
    y_midpoints = 0.5 * (recip_x_lin2[0:-1] + recip_x_lin2[1:])
    n_increments.append(n)
    areas.append(np.sum(y_midpoints*increment))


# Theoretical integral of 1/x from 1 to e = log(exp(1)) - log(exp(0)) = 1 - 0 = 1
integral = np.log(np.exp(1))-np.log(1)  # Answer

fig = plt.figure()
plt.plot(n_increments, areas, 'rx:')
plt.plot([n_increments[0], n_increments[-1]], [integral, integral], 'b:')
plt.xlabel("Number of intervals (n)")
plt.ylabel("Integral of 1/x")
plt.title(f"Integral of 1/x from 1 to e (first.last.yy)")
fig.savefig(os.path.join("data", "integration_recip_integral_1_to_e.png"))

plt.show()