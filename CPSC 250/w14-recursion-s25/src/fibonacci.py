"""
  Calculate Fibonacci value using both loop and recursion

  @author <your name here>
  @version 0
 """


class Fibonacci:

    def __init__(self):
        # Initialize counters
        self.loop_count = 0
        self.recursion_count = 0

    def fibonacci_loop(self, n):
        """
        Calculate value of Fibonacci sequence at given index
        using a loop (150 style)
            Raise a IndexError if n < 0
        :param n: index
        :return: value at index
        """
        if n < 0:
            raise IndexError("Number cannot be less than 0")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            current = 0
            previous = 1
            temp = 0
            for _ in range(n):
                temp = current
                current += previous
                previous = temp
            return current

    def fibonacci_recursion(self,n):
        """
        Calculate value of Fibonacci sequence at given index
        using recursion (250 style)
            Raise a IndexError if n < 0
        :param n: index
        :return: value at index
        """
        if n < 0:
            raise IndexError("Number cannot be less than 0")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci_recursion(n - 1) + self.fibonacci_recursion(n - 2)



if __name__ == '__main__':

    print("  index     loop (count)   recursion (count)")
    for i in range(16):
        fib=Fibonacci()
        print(" fib[{:2d}] = {:15d}({:3}) {:15d} ({:3d})".format(i,
                                               fib.fibonacci_loop(i),fib.loop_count,
                                               fib.fibonacci_recursion(i), fib.recursion_count))

