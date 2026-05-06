import matplotlib.pyplot as plt
import struct
import os


def plot_star_data(filepath):
    """
    Given a valid filepath, you will read a binary file that consists of two "columns" of double precision floating point numbers.
    The format is little endian. Once you have read the data plot the first column vs the second column (x axis is the first column).

    You should always properly label your plot!
        - In this case since there are no units you can title the x and y axes "x" and "y".
        - The title should be "Star Plot - (first.last.yy)"
        - Turn in this figure to scholar

    Hint: You will know that you are plotting the data correctly if the name of this function makes sense.

    :param filepath:
    :return:
    """
    with open(filepath, 'rb') as file:
        ba = file.read()
        x_data = []
        y_data = []
        format = '<dd'
        chunk_size = struct.calcsize(format)
        n_chunks = len(ba) // chunk_size
        for i in range(n_chunks):
            x_temp, y_temp = struct.unpack(format,ba[i*chunk_size:(i+1)*chunk_size])
            x_data.append(x_temp)
            y_data.append(y_temp)

        fig = plt.figure()
        plt.plot(x_data,y_data)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("star plot - Ryan.Schatzberg.24")
        plt.show()




if __name__ == "__main__":
    file = os.path.join("data", "star.dat")
    plot_star_data(file)
