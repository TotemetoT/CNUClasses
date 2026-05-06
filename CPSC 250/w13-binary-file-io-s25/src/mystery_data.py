"""
Sample file for binary I/O
"""

# Follow along in class as we analyze the mystery data in file

import os
import struct
import numpy as np
import math
import binascii
import matplotlib.pyplot as plt

format = '>iii'
b0 = []
b1 = []
b2 = []

with open(os.path.join('data','mystery_data.dat'), 'rb') as file:
    ba = file.read()
    chunk_size = struct.calcsize(format)
    num_chunks = len(ba) // chunk_size
    chunk0 = ba[0:]
    chunk1 = ba[1*chunk_size:2*chunk_size]
    for i in range(num_chunks):
        chunk = ba[1*chunk_size:(i+1)*chunk_size]
        v0 = struct.unpack(format, ba[i*chunk_size:(i+1)*chunk_size])
        if i < 10:
            print("{}{}".format(binascii.hexlify(chunk),v0))
        b0.append(v0[0])
        b1.append(v0[1])
        b2.append(v0[2])

    # Convert whole seconds and whole nanoseconds to seconds (as a float)
    ts = np.array(b0) - b0[0] + 1e-9*np.array(b1)
    ang = np.array(b2)*2*math.pi / 1024
    ang[ang>math.pi] = ang[ang>math.pi] - 2*math.pi

fig = plt.figure()
plt.plot(ts, ang)
plt.show()
