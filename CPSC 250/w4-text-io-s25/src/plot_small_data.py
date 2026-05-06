"""
Read in small data from file,and plot the output

Demo in class

"""
import matplotlib.pyplot as plt
import os
from src import small_data

file_path = os.path.join("data","small_data.txt")
linear, quadratic, cubic = small_data.read_data(file_path)

fig = plt.figure() #Open canvas
# plt.xkcd()  #Not Necessary
# plt.plot(linear,linear,'rx',label='linear')
# plt.plot(quadratic,quadratic,'rx',label='quadratic')
plt.plot(linear,cubic,'rx',label='cubic')
plt.show()