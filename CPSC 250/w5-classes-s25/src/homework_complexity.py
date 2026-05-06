import matplotlib.pyplot as plt
from numpy.random import exponential

"""
Homework in Complexity calculations and plotting.

"Complexity" of algorithms is a big part of computer science.
As the number of elements gets "large", some algorithms that are
overly complex may take too long.

You'll study complexity in advanced classes, but let's practice
file I/O and plotting and visualize the complexity values here.


For range of 1 to 30 (inclusive),
calculate

i, i*i, i**3, math.pow(2, i), math.log(i), math.log(i)*i

These are the
"linear, quadratic, cubic, exponential, logarithmic, and i*log(i)"
values


1) Write this data to a file in data folder
2) Read data back in and return values
3) Plot several ways as shown in lecture slides.

For some plots, you'll need to only plot a subset of data to keep in reasonable
range.


"""
import csv
import math
import os
import sys
import matplotlib.pyplot as plt


def write_complexity_to_file(file_path):
    """
    From i = 1 to 30 inclusive, write
    i  i*i  i**3  math.pow(2, i)  math.log(i)  math.log(i)*i

    to file using delimiter of your choice

    :param file_path : the file name with relative path information
    :return True if successful, False otherwise
    """
    with open(file_path, 'wt', newline='') as fin:
        writer = csv.writer(fin, delimiter="|")
        for i in range(1, 31):
            writer.writerow([i, i * i, i * i * i,math.pow(2, i), math.log(i), math.log(i)*i])
        return True


def read_complexity_data_from_file(file_path):
    """
    :param file_path : the file name with relative path information
    :return tuple of complexity data lists
    """
    c0, c1, c2, c3, c4, c5 = [], [], [], [], [], []
    with open(file_path, 'rt') as file_out:
        reader = csv.reader(file_out, delimiter='|')
        for data in reader:
            c0.append(int(data[0]))
            c1.append(int(data[1]))
            c2.append(int(data[2]))
            c3.append(float(data[3]))
            c4.append(float(data[4]))
            c5.append(float(data[5]))
    return c0, c1, c2, c3, c4, c5


if __name__ == '__main__':
    # Phase 1 - Write data to a file
    FILE_PATH = os.path.join("data", "complexity.csv")

    if not write_complexity_to_file(FILE_PATH):
        print("Failed to write complexity data!")
        sys.exit(-1)  # This terminates the script
    else:
        print("successfully wrote data")

    # Initially treat as a tuple with data that you choose
    complexity_data = read_complexity_data_from_file(FILE_PATH)
    if complexity_data is None or len(complexity_data) == 0:
        print("Failed to read complexity data!")
        sys.exit(-1)  # This terminates the script


    # Split the tuple
    linear, quadratic, cubic, exp, log, nlogn = complexity_data
    #
    # plt.figure(figsize=(6, 4))
    # plt.plot(linear, linear, 'ro', label='Linear')
    # plt.xlabel("i")
    # plt.ylabel("Linear (i)")
    # plt.title("Linear Complexity")
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    #
    # # Quadratic Plot
    # plt.figure(figsize=(6, 4))
    # plt.plot(quadratic, quadratic, 'go', label='Quadratic')
    # plt.xlabel("i^2")
    # plt.ylabel("Quadratic (i^2)")
    # plt.title("Quadratic Complexity")
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    #
    # # Cubic Plot
    # plt.figure(figsize=(6, 4))
    # plt.plot(cubic, cubic, 'bo', label='Cubic')
    # plt.xlabel("i^3")
    # plt.ylabel("Cubic (i^3)")
    # plt.title("Cubic Complexity")
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    #
    # # Exponential Plot
    # plt.figure(figsize=(6, 4))
    # plt.plot(exp, exp, 'ro', label='Exponential')
    # plt.xlabel("2^i")
    # plt.ylabel("Exponential (2^i)")
    # plt.title("Exponential Complexity")
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    #
    # # Logarithmic Plot
    # plt.figure(figsize=(6, 4))
    # plt.plot(log, log, 'go', label='Logarithmic')
    # plt.xlabel("log(i)")
    # plt.ylabel("Logarithmic (log(i))")
    # plt.title("Logarithmic Complexity")
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    #
    # # NlogN Plot
    # plt.figure(figsize=(6, 4))
    # plt.plot(nlogn, nlogn, 'bo', label='Natural Log')
    # plt.xlabel("i * log(i)")
    # plt.ylabel("Natural Log (i * log(i))")
    # plt.title("NlogN Complexity")
    # plt.legend()
    # plt.grid(True)
    # plt.show()

    # Linear Plot
    plt.figure(figsize=(6, 4))
    plt.plot(linear, linear, 'ro-', label='Linear')
    plt.xlabel("i")
    plt.ylabel("Linear (i)")
    plt.title("Linear Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Quadratic Plot
    plt.figure(figsize=(6, 4))
    plt.plot(linear, quadratic, 'go-', label='Quadratic')
    plt.xlabel("i")
    plt.ylabel("Quadratic (i^2)")
    plt.title("Quadratic Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Cubic Plot
    plt.figure(figsize=(6, 4))
    plt.plot(linear, cubic, 'bo-', label='Cubic')
    plt.xlabel("i")
    plt.ylabel("Cubic (i^3)")
    plt.title("Cubic Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Exponential Plot
    plt.figure(figsize=(6, 4))
    plt.plot(linear, exp, 'ro-', label='Exponential')
    plt.xlabel("i")
    plt.ylabel("Exponential (2^i)")
    plt.title("Exponential Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Logarithmic Plot
    plt.figure(figsize=(6, 4))
    plt.plot(linear, log, 'go-', label='Logarithmic')
    plt.xlabel("i")
    plt.ylabel("Logarithmic (log(i))")
    plt.title("Logarithmic Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()

    # NlogN Plot
    plt.figure(figsize=(6, 4))
    plt.plot(linear, nlogn, 'bo-', label='NlogN')
    plt.xlabel("i")
    plt.ylabel("NlogN (i * log(i))")
    plt.title("NlogN Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()

