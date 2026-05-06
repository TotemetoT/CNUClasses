"""

We will practice file I/O while having some fun with trigonometry

"""

import csv
import math
import os
import sys


def write_angle_data(file_path, increment=1):
    """
    We will write angle data for angles in degrees,
    the equivalent in radians, and the sine and cosine of the angles
    using the math.sin and math.cos methods

    Start at 0 degrees, and go to 360 degrees inclusive at the
    specified increment

    :param file_path: file name and path to write data
    :param increment: increment in whole degrees (e.g. 1 deg, 10 degrees)
    :return: True if successful, False otherwise
    """
    data = []
    #data = [100,180/pi*100]
    for deg in range(0,360+1,increment):
        rad = deg*math.pi/180
        data.append([deg,rad,math.sin(rad),math.cos(rad)])

    with open(file_path, 'wt', newline='') as fout:
        writer = csv.writer(fout,delimiter='\t')
        writer.writerow(data)

    return True

def read_angle_data(file_path):
    """
    Read angle data from file as:
    degrees , radians, sine, cosine

    :param file_path: file name and path to write data
    :return : numeric angle data in your choice of organization
    """
    angle = []
    with open(file_path, 'rt') as fin:
        reader = csv.reader(fin,delimiter='\t')
        for line in reader:
            angle.append((int(line[0]),float(line[1]),float(line[2]),float(line[3])))
    return angle

if __name__ == '__main__':

    file_path = os.path.join("data", "angle_data.csv")
    print(" Data file: ", file_path)

    if not write_angle_data(file_path, 20):
        print("Failed to write angle data!")
        sys.exit(-1)  # This terminates the script
    else:
        print("successfully wrote angle data")

    angle_data = read_angle_data(file_path)
    if angle_data is None or len(angle_data) == 0:
        print("Failed to read angle data!")
        sys.exit(-1)  # This terminates the script


    ## Now output the angle data using loop
    ## Maybe add a fancy header
    ## Make sure our data output is meaningful and lines up nicely
    print(f'\n{'deg':3}{'rad':^5}{'sin':^5}{'cos':^5}')
    print(20*'-')
    for item in angle_data:
        print(f'{item[0]:3d} {item[1]:5.3f} {item[2]:5.3f} {item[3]:5.3f}')

