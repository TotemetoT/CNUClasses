"""
  Calculate factorial using both loop and recursion

  @author <your name here>
  @version 0
 """
from scipy.special import factorial


def factorial_loop(n):
    """
      Calculate factorial using a loop (150 style)
        Raise a ValueError if n < 0
    :param n: number
    :return: n!
    """
    if n < 0: raise ValueError("Number cannot be less than 0")
    elif n == 0: return 1
    fact = 1
    for p in range(1,n+1):
        fact *= p
    print("returning loop fact")
    return fact


def factorial_recursion(n):
    """
    Calculate factorial using recursion (250 style!)
        Raise a ValueError if n < 0
    :param n:
    :return: n!
    """
    if n < 0:
        raise ValueError("Number cannot be less than 0")
    elif n == 0:
        return 1
    else:
        return n * factorial_recursion(n - 1)



if __name__ == '__main__':
    for i in range(16):
        print(" {:2d}! = {:15d} {:15d}".format(i, factorial_loop(i), factorial_recursion(i)))
