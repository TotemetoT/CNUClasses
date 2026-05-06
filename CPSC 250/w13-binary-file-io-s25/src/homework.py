import struct
import os
# from contextlib import suppress


def read_attributes(file_path, formatting):
    """
    Given a binary file written using struct.pack() with the given format,
    return the number of bytes in the file and the number of bytes in each chunk.

    :param file_path:
    :param formatting: a string with the format of the data in the struct
    :return: tuple with the number of bytes in file and the number of bytes written in each chunk
    """
    size = struct.calcsize(formatting)
    with open(file_path, 'rb') as fin:
        data = fin.read()
    return len(data), size




def read_binary_file(file_path):
    """

    Read a binary file that is formatted using little endian format and that has one integer and 3 doubles in that order.
    Return 4 lists (In the same order that you read the columns).

    :param file_path:
    :return:
    """
    val0, val1, val2, val3 = [],[],[],[]
    fmt = '<iddd'
    chunk_size = struct.calcsize(fmt)
    with open(file_path, 'rb') as fin:
        while chunk := fin.read(chunk_size):
            unpacked = struct.unpack(fmt, chunk)
            int_val, d1, d2, d3 = unpacked
            val0.append(int_val)
            val1.append(d1)
            val2.append(d2)
            val3.append(d3)
    return val0, val1, val2, val3



if __name__ == '__main__':
    print(read_attributes(os.path.join("data", "binary.dat"), ">iid"))
    print(read_binary_file(os.path.join("data", "binary.dat")))
