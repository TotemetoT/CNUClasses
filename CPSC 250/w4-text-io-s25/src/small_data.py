"""
Demo some reading of files

Modify your Run-Edit Configuration to point to the project folder, not src!
"""
import os


def read_data(fpath):
    """
    Read data from file into 3 columns  c0|c1|c2
    :param fpath:
    :return: c0,c1,c2
    """
    with open(fpath,'rt') as file:
        lines = file.readlines()

    c0,c1,c2 = [],[],[]

    for line in lines:
        data = line.split("|")
        c0.append(int(data[0]))
        c1.append(int(data[1]))
        c2.append(int(data[2]))
    return c0,c1,c2


def append_data(file_path, max_val=32):
    """
    Add up to i=max_val for i|i^2|i^3
    :param file_path:
    :return: Number of lines written to the file
    """
    c1, _, _ = read_data(file_path)
    mx = 0
    if len(c1) > 0:
        mx = max(c1)
    else:
        return 0
    with open(file_path,'at') as fin:
        data = []
        for i in range(mx+1,max_val+1):
            data.append("{}|{}|{}\n".format(i,i*i,i*i*i))

        fin.writelines(data)
        return len(data)


def write_data(file_path, start_val=0, end_val=32):
    """
    Write file with i|i^2|i^3 from start_val to end_val (inclusive)
    If file already exists, just overwrite it

    :param file_path:
    :return: Number of lines written to the file
    """
    with open(file_path,'wt') as file:
        data = []
        for i in range(start_val,end_val+1):
            data.append("{}|{}|{}\n".format(i,i*i,i*i*i))
        file.writelines(data)
        return len(data)


if __name__ == '__main__':
    file_path = os.path.join("data", "small_data.txt")
    print("path:", file_path)

    # Get me 3 lists of integers
    c1, c2, c3 = read_data(file_path)
    print(c1)
    print(c2)
    print(c3)


    num_lines = append_data(file_path)
    print(f"wrote {num_lines} lines to file")

    c1, c2, c3 = read_data(file_path)

    print(c1)
    print(c2)
    print(c3)

    num_lines = write_data(file_path, 1, 10)
    print(f"wrote {num_lines} lines to file")

    c1, c2, c3 = read_data(file_path)

    print(c1)
    print(c2)
    print(c3)
