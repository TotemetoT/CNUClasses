"""

Numpy and MatPlotLib

Calculate and plot the amount of Carbon-14 present in a fossil as a function of time
using Numpy and MatPlotLib.


The 1/2 life of C-14 is 5730 years.

The `decay` rate is given by the natural logarithm of 2 divided by the 1/2 life in years.

Use the `log` function (either `math` or `numpy` versions) for natural log (e.g., `math.log(2)`)

That is decay rate equals math.log(2) divided by 5730 

The amount of C-14 is given by the exponential function with negative exponent

    mass*exp(-decay*time) for each time in the time vector


Assuming the animal started with 10 kg of C-14 in the sample, plot the expected
amount to remain over the next 50,000 years.
NOTE: The plotted value should get smaller as time increases

Use a time range of 0 to 50,000 years, with an increment of 100 years.

Label and title your plot.

Don't overthink this.

 It is intended to be simple, and relatively quick.

 The entire solution needs less than 10 lines of code.

    @author Ryan Schatzberg
"""

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    import numpy as np
    import matplotlib.pyplot as plt

    if __name__ == '__main__':
        half_life = 5730
        decay = np.log(2) / half_life  # Proper decay rate
        time = np.arange(0, 50001, 100)  # Time from 0 to 50,000 years
        initial_mass = 10  # in kg
        remaining_mass = initial_mass * np.exp(-decay * time)  # Decay formula

        plt.plot(time, remaining_mass)
        plt.xlabel('Time (years)')
        plt.ylabel('C-14 Remaining (kg)')
        plt.title('Carbon-14 Decay Over Time')
        plt.grid(True)
        plt.show()

