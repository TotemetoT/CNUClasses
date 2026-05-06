"""
 * We will use this to test some different exception types
 *
 * @author dconner
 * @version 0
 *
 */
"""

from src.my_very_own_error import MyVeryOwnError


class Exceptions:

    @staticmethod # Decorator to define methods that don't use instance or class methods, and therefore don't need self, or cls arguments
    def throw_something(val):
        """
        See https://docs.python.org/3/library/exceptions.html
        Return the val, UNLESS:
            val<0, then raise a ValueError,
            val==0, then raise a OSError
            val==1, then raise a FileNotFoundError
            val==2, then raise a MyNewError

        HINT: It will be helpful to you to look at the required messages in catchSomething

        :param val:
        :return: val, unless one of above Exceptions
        """

        if val < 0:
            raise ValueError("Negative values are not allowed")
        elif val == 0:
            raise OSError("OS error")
        elif val == 1:
            raise FileNotFoundError("File not found")
        elif val == 2:
            raise MyVeryOwnError("My very own message")
        return val

    @staticmethod
    def catch_something(val):
        """
        This method should not fail regardless of val passed, and should return the following:

        If val < 0, return "Negative values are not allowed"
        if val == 0, return "OS error"
        If val == 1, return ("File not found", 1) NOTE: This one requires a tuple to be returned!
        if val == 2, return "My very own message"

        Otherwise, return the string corresponding to the value

        DO NOT Modify the code in the designated block delimited by # vvvv #^^^^^.
        :return: string
        """
        ## You may modify the below line with a single line of code (this added to preserve indenting)
        try: # You may this single line as needed as long as throwSomething is always called!
            ### vvvvvvv DO NOT MODIFY THIS BLOCK OF CODE vvvvvvvvvvvv
            Exceptions.throw_something(val)
            ### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        except ValueError as e:
            print("Caught value error! ", e)
            return str("Negative values are not allowed")
        except FileNotFoundError as e:
            return (str(e), 1)
        except Exception as e:
            return str(e)
        # You may add whatever code is necessary down here, but the above throwSomething method must be called first!
        return str(val)

