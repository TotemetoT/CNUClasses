"""
Some miscellaneous functions to help us along the way
"""
import numpy as np
import matplotlib.pyplot as plt
def plot_trapezoids(x_values, y_values):
    """
    Given active Matplotlib figure,
    Plot trapezoids from x-axis to points on array,
    and rectangles to midpoints
    :param x_values:
    :param y_values:
    :return: array of midpoint values for approximate numerical integration
    """
    x_midpoints = 0.5*(x_values[0:-1] + x_values[1:])
    y_midpoints = 0.5*(y_values[0:-1] + y_values[1:])
    for i in range(0,len(x_values)-1):
        x_box  = [x_values[i], x_values[i], x_values[i+1], x_values[i+1]]
        y_box  = [0.0, y_values[i],    y_values[i+1],    0.0]
        ym_box = [0.0, y_midpoints[i], y_midpoints[i], 0.0]

        plt.plot(x_box, y_box, 'g-', linewidth=2)
        plt.plot(x_box, ym_box, 'b:', linewidth=2)
        plt.plot(x_midpoints[i], y_midpoints[i], 'bo', linewidth=2)

    plt.plot(x_values, y_values, 'r*:', linewidth=2)
    return x_midpoints, y_midpoints




def cumulative_summation(array):
    # I refuse to use this Numpy function name around anyone
    # who has been to middle school
    return np.cumsum(array)
