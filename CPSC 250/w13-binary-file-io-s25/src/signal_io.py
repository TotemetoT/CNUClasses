import os
import struct
import csv
# from signal import signal

import numpy as np


def write_csv_as_binary(file_name, folder_name="data"):
    """
    Read in data from CSV file, and resave as binary.
    :param folder_name: Folder where CSV file is located
    :param file_name: CSV file name (without extension)
    :return: seconds, nanoseconds, signal_data lists
    """
    seconds = []
    nanoseconds = []
    signal_data = []

    file_path = os.path.join(folder_name, file_name + ".csv")
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        line_reader = csv.reader(csv_file, delimiter=',')
        for line in line_reader:
            if len(line) > 0:
                seconds.append(int(line[0]))
                nanoseconds.append(int(line[1]))
                signal_data.append(float(line[2]))

    binary_data = bytearray()
    for sec, nano, sig in zip(seconds, nanoseconds, signal_data):
        binary_data += struct.pack(">iid", sec, nano, sig)

    new_path = os.path.join(folder_name, file_name + ".dat")
    with open(new_path, 'wb') as f:
        f.write(binary_data)

    return seconds, nanoseconds, signal_data


def read_binary(file_name, folder_name="data"):
    """
    Read binary file data
    :param folder_name:
    :param file_name: filename
    :return: seconds, nanoseconds, signal_data data from csv file as lists
    """
    fpath = os.path.join(folder_name, file_name + ".dat")
    with open(fpath, 'rb') as fout:
        my_bytearray = fout.read()

    chunk_size = struct.calcsize('>iid')
    seconds = []
    nanoseconds = []
    signal_data = []
    for i in range(len(my_bytearray) // chunk_size):
        start = i * chunk_size
        end = start + chunk_size
        data = struct.unpack('>iid', my_bytearray[start:end])
        seconds.append(data[0])
        nanoseconds.append(data[1])
        signal_data.append(data[2])

    return seconds, nanoseconds, signal_data


def convert_data(seconds, nanoseconds, signal_data):
    """
    Convert epoch timestamp into zero referenced float
    :param signal_data:
    :param seconds: whole seconds since Jan 1, 1970
    :param nanoseconds: nanoseconds since whole second
    :return: time and signal_data as two float numpy arrays
    """
    seconds = np.asarray(seconds, dtype=np.int64)
    nanoseconds = np.asarray(nanoseconds, dtype=np.int64)
    signal_data = np.asarray(signal_data, dtype=np.float64)

    time = (seconds - seconds[0]).astype(np.float64) + nanoseconds.astype(np.float64) * 1e-9

    time = np.round(time, 9)

    return time, signal_data


if __name__ == "__main__":
    write_csv_as_binary("signal_data", "data")
