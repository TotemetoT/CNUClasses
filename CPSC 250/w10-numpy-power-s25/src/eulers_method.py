import numpy as np
import os
import scipy.special  # Special scientific calculations
import sys
import matplotlib.pyplot as plt


skip = 5  # Skipping fewer points and using more samples (smaller increment) gives better approximation
x_lin = np.linspace(0, 3, 50)  # Try skipping fewer points and more than 50 spacing
ex_lin = np.exp(x_lin)

fig = plt.figure()
plt.plot(x_lin, ex_lin, 'r*:')
plt.xlabel("x")
plt.ylabel("exp(x)")
plt.title("Euler's method (first.last.yy)")
fig.savefig(os.path.join("data", "eulers_linear.png"))

# Comment out the next two lines to continue
plt.show()
sys.exit(-1)

x_euler = x_lin[::skip]  # Skip some points

dt = x_euler[1]-x_euler[0]
print("Time step = ", dt)

# Set up arrays to hold our data
fwd_euler = np.zeros(x_euler.shape)
back_euler = np.zeros(x_euler.shape)
mid_euler = np.zeros(x_euler.shape)

# Assume know starting point
fwd_euler[0] = ex_lin[0]
back_euler[0] = ex_lin[0]
mid_euler[0] = ex_lin[0]

for ndx in range(1,len(x_euler)):

    # Forward Euler with known derivative exp(x)
    fwd_euler[ndx] = fwd_euler[ndx-1] + np.exp(x_euler[ndx-1])*dt

    # Backward Euler is an "implicit" function.  Normally the derivative might
    # depend on the y-value at the end point, so we have chicken-egg problem
    # that requires iteration to convergence.
    # For our simple exponential we know the derivative at end point directly

    # Backward Euler with known end point derivative exp(x)
    back_euler[ndx] = back_euler[ndx-1] + np.exp(x_euler[ndx])*dt

    # Euler using known derivative at mid-point exp(x)
    mid_euler[ndx] = back_euler[ndx-1] + np.exp(x_euler[ndx-1]+0.5*dt)*dt

fig = plt.figure()
plt.plot(x_lin, ex_lin, 'r-', label='ideal')
plt.plot(x_euler, fwd_euler, 'b*:', label='Fwd Euler')
plt.plot(x_euler, back_euler, 'g*:', label='Backward Euler')
plt.plot(x_euler, mid_euler, 'm*:', label='Midpoint Euler')
plt.xlabel("x")
plt.ylabel("exp(x)")
plt.legend()
plt.title(f"Euler's method dt={dt:.3f} (first.last.yy)")
fig.savefig(os.path.join("data", "eulers_method.png"))

plt.show()