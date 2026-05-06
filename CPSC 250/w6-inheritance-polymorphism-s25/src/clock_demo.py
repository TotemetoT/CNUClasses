import datetime
import time

class Clock:
    """
    Class to print the time with varying precision
    """

    #Static class variables
    minute_precision = 'minutes'
    second_precision = 'seconds'
    microsecond_precision = 'microsecond'

    def __init__(self, precision=minute_precision):
        """
        Constructor for Clock class. The precision defaults to minute precision
        :param precision: the precision of this clock
        """
        # start time at midnight by default
        self.__precision = precision

    def get_time(self):
        """
        Method to create a return a string representing the current time
        :return: a string representing the curren time
        """
        now = datetime.datetime.now()
        time_string = str(now.hour) + ":" + str(now.minute)
        if self.__precision == Clock.minute_precision:
            return time_string
        if self.__precision == Clock.second_precision:
            return time_string + ":" + str(now.second)
        if self.__precision == Clock.microsecond_precision:
            return time_string + ":" + str(now.second) + ":" + str(now.microsecond)


    def set_precision(self, precision):
        """
        Method to set the precision of this clock object
        :param precision: the precision to set the clock to. Must be Clock.minutes, Clock.seconds, or Clock.microseconds
        :return: None
        """
        #Check to make sure a valid precision is passed in
        if precision != Clock.minute_precision and precision != Clock.second_precision \
                and precision != Clock.microsecond_precision:
            print("ERROR: incorrect precision string")
        self.__precision = precision


class AlarmClock(Clock):
    """
    Derived Class from Clock. Adds alarm functionality
    """

    def __init__(self, precision=Clock.minute_precision):
        """
        Constructor for alarm clock class.

        :param precision: the prevision of this clock
        """
        #The first thing to do (almost always) when creating a derived class is to call the base class's constructor
        # this will set all the base class attributes.
        Clock.__init__(self, precision=precision)

        #The next step is to set the derived class attributes, and make any changes to the base class attributes
        # that you want. In this case, I don't have any changes to the base class attributes (__precision), so I
        # just set the derived class attributes
        self.__alarm_hours = 0
        self.__alarm_minutes = 0
        self.__alarm_on = False

    def set_alarm(self):
        pass

    def toggle_alarm(self):
        pass


if __name__ == '__main__':
    #This code uses the datetime class
    # datetime.datetime.now() returns an object
    # https://docs.python.org/3/library/datetime.html
    now = datetime.datetime.now()
    print("dir(now) = ", dir(now))

    #create clock 1, print its time, change the precision and print the time again
    print("\ncreate clock 1, print its time, change the precision and print the time again")
    clock1 = Clock()
    print("clock 1 says: ", clock1.get_time())
    clock1.set_precision(Clock.second_precision)
    print("clock 1 says: ", clock1.get_time())

    #We can specify the precision in the constructor. The preferred way is to use the class constant variables
    print("\nWe can specify the precision in the constructor. The preferred way is to use the class constant variables")
    clock2 = Clock(precision=Clock.second_precision)
    # ... however, we can also use the string that defines the variables
    clock3 = Clock(precision='microsecond')
    time.sleep(1)
    print("clock 2 says: ", clock2.get_time())
    time.sleep(0.1)
    print("clock 3 says: ", clock3.get_time())
    time.sleep(1)

    #Each instance of clock can have different precisions, and it doesn't affect the other instances of clock
    # the data held by each instance is specific to it
    print("\nEach instance of clock can have different precisions, and it doesn't affect the other "
           "instances of clock the data held by each instance is specific to it")
    clock1.set_precision(Clock.minute_precision)
    print("clock 1 says: ", clock1.get_time())
    print("clock 2 says: ", clock2.get_time())
    print("clock 3 says: ", clock3.get_time())
