"""
Practice File I/O  (input/output) using an angle degrees to radians conversion
@author <your name here>
"""
import csv
import math
import numpy as np
from rdkit.Contrib.LEF.AddLabels import delim


def write_angles(file_path):
    """
    Write file containing whole degrees (0 - 360) in 1 degree increments and
    equivalent degree in radians.
    Use one line per angle, and separate numbers with a tab character ('\t').

    :param file_path: Whole path to file location to write data
    :return : Nothing to return
    """

    # Write out some comments about the steps you need to take to solve

    # write the the code
    degs =  np.arange(0.0,361.0,1)
    print("deg = ", degs)

    rads = (math.pi/180.0)*degs

    with open(file_path,"wt") as file:
        writer = csv.writer(file, delimiter="\t")
        for i in range(len(degs)):
            writer.writerow((degs[i],rads[i]))


def read_angles(file_path):
    """
    Write file containing whole degrees (0 - 360) in 1 degree increments and
    equivalent degree in radians.
    :param file_path: Whole path to file location to read data
    :return : Tuple containing two numpy arrays degrees, and radians
    """
    # Write out some comments about the steps you need to take to solve

    # write the the code
    with open(file_path,'rt') as file:
        reader = csv.reader(file,delimiter='\t')
        degs = []
        rads = []

        for data in reader:
            degs.append(float(data[0]))
            rads.append(float(data[0]))

    return np.array(degs),np.array(rads)

if __name__ == '__main__':

    import os
    relative_file_path = os.path.join("data", "angles_module.txt")
    print(" File:", relative_file_path)

    write_angles(relative_file_path)

    degs, rads = read_angles(relative_file_path)
    print("  Type: ", type(degs), type(rads))
    print("Degree Equivalents:")
    print("{:>5s}: {:>8s} : {:>8s}".format("Angle", "Degrees", "Radians"))
    for i, deg in enumerate(degs):
        print(" {:3d} : {:8.2f} : {:8.4f}".format(i, deg, rads[i]))
