import numpy as np
import os
import scipy.special  # Special scientific calculations
import sys
import matplotlib.pyplot as plt
from given.special_functions import plot_trapezoids

x_lin = np.linspace(0, 3, 10)
ex_lin = np.exp(x_lin)


fig = plt.figure()
plt.plot(x_lin, ex_lin, 'r*:')
plt.xlabel("x")
plt.ylabel("exp(x)")
#plt.axis('equal')
plt.title("exp(x) - Linear Scale! (first.last.yy)")
fig.savefig(os.path.join("data", "derivatives_exp.png"))

fig = plt.figure()
plt.plot(x_lin, ex_lin, 'r*:')
plt.quiver(x_lin, ex_lin, np.ones(x_lin.shape), ex_lin,color='b')
plt.xlabel("x")
plt.ylabel("exp(x)")
plt.axis('equal')  # Need this for arrows to look correct by scale
plt.title("exp(x) - Quiver (first.last.yy)")
fig.savefig(os.path.join("data", "derivatives_quiver.png"))

# Comment out the next two lines to continue
plt.show()
sys.exit(-1)

increment = 0.125 #/10
x_der = np.arange(0.75, 1.26, increment)
ex_der = np.exp(x_der)

ndx = int(len(x_der)*0.7)  # Pick a point
print("Ndx = ", ndx)

# Change in x (dx)
dx = x_der[ndx+1] - x_der[ndx] # Better be increment of above!

# Change in y
dy = ex_der[ndx+1] - ex_der[ndx]

# dy/dx approximate derivative specifies change in y value per unit change in x value
dy_dx = dy/dx
print(f"Approximate derivative({x_der[ndx]}) = {dy_dx:.4f} = {ex_der[ndx]}")

fig = plt.figure()
plt.plot(x_der, ex_der, 'r+:', label='exp(x)')
plt.quiver(1.0, np.exp(1), 1, np.exp(1), color='b')
plt.quiver(x_der[ndx], ex_der[ndx], 1, dy_dx, color='g')

plt.xlabel("x")
plt.ylabel("exp(x)")
plt.axis('equal')
plt.title("exp(x) derivatives (first.last.yy)")
fig.savefig(os.path.join("data", "derivatives_approximate.png"))

# Comment out the next two lines to continue
plt.show()
sys.exit(-1)


# Compare with 2^x and 3^x
# exp(x) is it's own derivative without scaling

a2x_der = np.power(2.0, x_der)
a3x_der = np.power(3.0, x_der)

plt.plot(x_der, a2x_der, 'gx:', label='2^x')
plt.plot(x_der, a3x_der, 'bx:', label='3^x')
plt.quiver(1.0, 2, 1, np.log(2)*2, color='g')  # Requires log(2) scaling for derivative
plt.quiver(1.0, 3, 1, np.log(3)*3, color='b')
plt.legend()
fig.savefig(os.path.join("data", "derivatives_others.png"))
plt.show()