"""
Practice numpy calculations
@author Ryan Schatzberg
"""
import numpy as np
import matplotlib.pyplot as plt


def create_dataset(x, max_val=7):
    """
    Return the sum of sin(n*x)/n where n = 1,2,3,4,5... max_val
    Remember, n is a scalar quantity (float/int). x is a NumPy array and you should return an equal length NumPy array

    :param x: numpy array
    :param max_val: The maximum value
    :return: a tuple with two numpy arrays x and the sum

    """
    sum_array = np.zeros_like(x, dtype=np.float64)  # Initialize with zeros

    for n in range(1, max_val + 1):
        sum_array += np.sin(n * x) / n  # Element-wise addition

    return x, sum_array


def generate_datasets(n, amp1, mean1, sigma1, amp2, mean2, sigma2):
    """
    First generate a linearly spaced numpy array called x from 0 to 1.0, inclusive of 0 and 1 with n number of points.
        Ex: For 5 data points your array should contain: [0.0, 0.25, 0.5, 0.75, 1.0]

    Then, generate two numpy arrays using the amp, mean, and sigma for a gaussian distribution (AKA: Normal distribution/Bell curve).
    You will use your x array as the x values for the gaussian functions.

    https://en.wikipedia.org/wiki/Gaussian_function (In the wiki version a=amplitude, b=mean, and c=sigma)
    Also, see the image in the README.md or the image located in the img folder: img/gaussian.png

    Note: Exponentials like e^x are really just like x^y where x is a constant number ~2.71828
        In numpy there are useful functions like np.exp(x) which would be e^x.
            -https://docs.scipy.org/doc/numpy/reference/generated/numpy.exp.html
        In addition, you may find that it would be useful to use np.power()
            -https://docs.scipy.org/doc/numpy/reference/generated/numpy.power.html

    :param amp1:
    :param mean1:
    :param sigma1:
    :param amp2:
    :param mean2:
    :param sigma2:
    :return: x, gaussian 1, and gaussian 2 in a tuple
    """
    x = np.linspace(0, 1, n)

    # Step 2: Compute the two Gaussian distributions
    gaussian1 = amp1 * np.exp(-np.power((x - mean1) / sigma1, 2) / 2)
    gaussian2 = amp2 * np.exp(-np.power((x - mean2) / sigma2, 2) / 2)
    # Step 3: Return x and the two Gaussian distributions
    return x, gaussian1, gaussian2



def plot_data(x, y, y2):
    """
    Given three numpy arrays: x, y, y2
    Create one figure with the following: x vs y (labeled "Pions"), x vs y2 (labeled "Kaons") and  vs the sum of y and y2 (labled "Sum").
    The title should contain your first.last.YY in parentheses and the title should be "Nuclear Physics"
    A legend should be used for full credit.

    Save your figure into the data folder and upload to scholar.

    :param x:
    :param y:
    :param y2:
    :return:
    """

    plt.plot(x,y, 'rd', label="Pions")
    plt.plot(x, y2, 'bd', label="Kaons")
    plt.plot(y, y2, 'gd', label="Sum")

    plt.title("Nuclear Physics")
    plt.suptitle("Ryan.Schatzberg.24")
    plt.legend()
    plt.show()


if __name__ == '__main__':

    #Some useful test functions for generate_datasets and one for plot_data
    # print(create_dataset(np.array([1,2,3,4,5]),5))
    x, y, y2 = generate_datasets(100, 1.0, .137, .05, .5, .495, .15)
    print(x)
    print(y)
    print(y2)
    plot_data(x, y, y2)
