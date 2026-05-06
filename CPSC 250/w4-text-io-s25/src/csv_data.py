"""
Do it all again, but this time use csv.reader and writer as appropriate

"""

import os
import csv



def write_data_csv(file_path, start_val=0, end_val=32):
    """
    Write file with i|i^2|i^3 from start_val to end_val (inclusive)

    If file already exists, just overwrite it

    :param file_path:
    :return: Number of lines written to the file
    """
    with open(file_path,'wt', newline = '') as fout:
        writer = csv.writer(fout,delimiter = "|")

        for i in range(start_val,end_val+1):
            writer.writerow([i,i*i,i*i*i])
    return end_val - start_val + 1

def read_data_csv(fpath):
    """
    Read data from file into 3 columns  c0|c1|c2
    :param fpath:
    :return: c0,c1,c2
    """
    c0, c1, c2 = [], [], []
    with open(fpath,'rt') as fin:
        reader = csv.reader(fin,delimiter='|')
        for data in reader:
            c0.append(int(data[0]))
            c1.append(int(data[1]))
            c2.append(int(data[2]))
    return c0,c1,c2


def append_data_csv(file_path, max_val=32):
    """
    Add up to i=max_val for i|i^2|i^3 starting from last line in current file
    :param file_path:
    :param max_val: ending point (inclusive) of last line
    :return: Number of lines written to the file
    """

    c1, _, _ = read_data_csv(file_path)
    if len(c1) > 0:
        max_in = len(c1)
    else:
        max_in = 0

    with open(file_path,'at', newline='') as fout:
        writer = csv.writer(fout,delimiter='|')
        for i in range(max_in,max_val+1):
            writer.writerow([i,i*i,i*i*i])
        return max_val - max_in+1

if __name__ == '__main__':

    fpath = os.path.join("data", "small_data.csv")
    print("path:", fpath)

    num_lines = write_data_csv(fpath, 1, 100)
    print(f"wrote {num_lines} lines to file")

    read_data_csv(fpath)

    c1, c2, c3 = read_data_csv(fpath)

    print(c1)
    print(c2)
    print(c3)

    #
    num_lines = append_data_csv(fpath)
    print(f"wrote {num_lines} lines to file")

    c1, c2, c3 = read_data_csv(fpath)

    print(c1)
    print(c2)
    print(c3)
