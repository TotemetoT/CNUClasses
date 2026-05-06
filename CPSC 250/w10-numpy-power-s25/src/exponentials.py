import numpy as np
import os
import scipy.special  # Special scientific calculations
import sys
import matplotlib.pyplot as plt


x_lin = np.linspace(0, 32, 50)
ex_lin = np.exp(x_lin)

fig = plt.figure()
plt.plot(x_lin, ex_lin, 'r*:')
plt.xlabel("x")
plt.ylabel("exp(x)")
plt.title("Exponential - Linear Scale! (first.last.yy)")
fig.savefig(os.path.join("data", "exponential_linear.png"))

fig = plt.figure()
plt.plot(x_lin, ex_lin, 'r*:')
plt.xlabel("x")
plt.ylabel("log")
plt.yscale('log')
plt.title("Exponential - Log Scale! (RYan.Schatzberg.24)")
fig.savefig(os.path.join("data", "exponential_logscale.png"))

# plt.show()
# sys.exit(-1)

x_log = np.logspace(-3,2,50)
print(x_log)
recip_x_log = 1/x_log
fig = plt.figure()
plt.plot(x_lin, recip_x_log, )



increment = 0.25
x_lin2 = np.arrange(0.25,5.,increment)
recip_x_lin2 = 1/x_lin2
fig = plt.figure()
plt.plot(x_lin2, recip_x_lin2, 'ko')
plt.xlabel('x')
plt.ylabel('1/x')
plt.title(f'Reciprocal 1/x area under curve for n={len(x_midpoints)}')