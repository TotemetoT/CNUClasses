import numpy as np
import os
import scipy.special  # Special scientific calculations
import sys
import matplotlib.pyplot as plt

from given.special_functions import cumulative_summation

print("Factorial with loops")
for i in range(1,6):
    val = 1
    for j in range(2, i+1):  # include i
        val *= j
    print(f"{i: 3d}! = {val}")


print(f"Factorial with Numpy")
fact_val = np.math.factorial(18)  # Takes a single integer
print(f" n=18, n!={fact_val}={fact_val: e}")

n_vals = np.arange(0, 19, dtype='int')
print("n vals =", n_vals)
print(dir(scipy))

fact_vals = scipy.special.factorial(n_vals) # factorials with numpy array
print(f"{'n':>3s}    {'n!':>20s} = {'n! (sci. notation)':>20s} ")
for i, n in enumerate(n_vals):
    print(f"{n: 3d}! = {fact_vals[i]:20.0f} = {fact_vals[i]:20e} ")

fig = plt.figure()
plt.plot(n_vals, fact_vals, 'r*:')
plt.xlabel("n")
plt.ylabel("n!")
plt.title("Factorials- Linear Scale! (first.last.yy)")
fig.savefig(os.path.join("data", "factorials_linear.png"))

# Comment out the next two lines to continue
plt.show()
sys.exit(-1)


#####################
# Demo of log scale plotting
#####################
fig = plt.figure()
plt.plot(n_vals, fact_vals, 'r*:')
plt.xlabel("n")
plt.ylabel("n!")
plt.yscale('log')  # Use logarithmic scale for y-axis
plt.title("Factorials - Log Scale! (first.last.yy)")
fig.savefig(os.path.join("data", "factorials_logscale.png"))

# Comment out the next two lines to continue
plt.show()
sys.exit(-1)

#########################
## Reciprocals 1/n!
#########################

recip_vals = 1/fact_vals

# Sum of all previous values in array so that output
# output = [input[0], input[0]+input[1], output[1]+input[2], output[2]+input[3], ...]
sum_previous = cumulative_summation(recip_vals)


print(f"{'n':>3s}    {'n!':>20s} = {'n! (sci. notation)':>20s} | {'1/n!':>20s} {'Sum(1/n!)':>20s}")
for i, n in enumerate(n_vals):
    print(f"{n: 3d}! = {fact_vals[i]:20.0f} = {fact_vals[i]:20e} | {recip_vals[i]:20f} {sum_previous[i]:20f}")

print(f"Cumulative summation of 1/n! = {sum_previous[-1]}")


fig = plt.figure()
plt.plot(n_vals, recip_vals, 'r*:')
plt.xlabel("n")
plt.ylabel("1/n!")
#plt.yscale('log')  # Use logarithmic scale for y-axis
plt.title("Reciprocals! (first.last.yy)")
fig.savefig(os.path.join("data", "reciprocals.png"))

fig = plt.figure()
plt.plot(n_vals, sum_previous, 'r*:')
plt.xlabel("n")
plt.ylabel("sum(1/n!)")
#plt.yscale('log')  # Use logarithmic scale for y-axis
plt.title("Cumulative summation of 1/n! (first.last.yy)")
fig.savefig(os.path.join("data", "cumulative_summation.png"))

plt.show()
