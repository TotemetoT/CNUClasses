
"""
Demo of Pickle module for simple binary I/O
"""

import os
import pickle
import random


class A:

    def __init__(self, data):
        self.data = data
        self.rand = random.randint(0, 1e9)

    def __str__(self):
        return str((self.data, self.rand))

    def __eq__(self, other):
        return self.data == other.data and self.rand == other.rand



def save_pickle(data_list, file_name):
    try:
        pickle.dump(data_list, open(os.path.join("data", file_name), 'wb'))
        return True
    except Exception as e:
        print(e)
        return False

def load_pickle(file_name):
    try:
        return pickle.load(open(os.path.join("data", file_name),'rb'))
    except Exception as e:
        print(e)


if __name__ == '__main__':

    data_list = [A('a'), A('B'), A(3)]
    #data_list = load_pickle("pickle_test.pkl")
    print("given data list: ", [str(dat) for dat in data_list])

    if not save_pickle(data_list, "pickle_test.pkl"):
        print("Failed to pickle")
    else:
        print("Saved to pickle")

        data_load = load_pickle("pickle_test.pkl")
        if data_load is None:
            print("Failed to load pickle")
        else:

            print(" Is same? ", data_load is data_list)
            print(" Is equal? ", data_load == data_list)
            print(" Is equal: ", [ a == data_list[i] for i, a in enumerate(data_load) ])
            print(" Is instance: ", [ a is data_list[i] for i, a in enumerate(data_load) ])
