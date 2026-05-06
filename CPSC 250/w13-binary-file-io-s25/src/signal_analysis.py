import os
import matplotlib.pyplot as plt
from src.signal_io import write_csv_as_binary, read_binary, convert_data

if __name__ == '__main__':
    seconds_text, nanoseconds_text, signal_data_text = write_csv_as_binary("signal_data")
    seconds_binary, nanoseconds_binary, signal_data_binary = read_binary("signal_data")
    time_list, signal_data_list = convert_data(seconds_binary, nanoseconds_binary, signal_data_binary)

    print(" seconds data:", seconds_text == seconds_binary)
    print(" nanoseconds data:", nanoseconds_text == nanoseconds_binary)
    print(" signal_data data:", signal_data_text == signal_data_binary)

    fig = plt.figure(1)
    plt.plot(time_list, signal_data_list, 'b-', label="signal", linewidth=2)
    plt.legend()
    plt.xlabel('time (s)')
    plt.ylabel('signal')
    plt.title('Signal Data (first.last.yy)')
    fig.savefig(os.path.join("data", "signal_data.png"))

    plt.show()
