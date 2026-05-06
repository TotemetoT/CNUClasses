"""
Practice File input and plotting using Matplot lib
@author <your name here>
"""

import angles_module
#import math
import matplotlib.pyplot as plt
import numpy as np
import os

# Read the file
relative_file_path = os.path.join("data", "angles_module.txt")
print(" File:", relative_file_path)
degs, rads = angles_module.read_angles(relative_file_path)
print("rads=", rads)

sin = np.sin(rads)

fig = plt.figure()
plt.plot(rads,sin,"b-", label="sine of rads")
plt.plot(degs,sin,'r*',label="sine of degs")
plt.xlabel("degrees")
plt.ylabel("sine function value")
plt.title("sine function (ryan.schatzberg.24)")
plt.grid(True, lw=1.0)
plt.tight_layout()
fig.savefig(os.path.join('data','sine_angle_module.png'))
plt.show()