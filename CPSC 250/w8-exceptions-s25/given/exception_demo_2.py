
class ExceptionDemo2:
    @staticmethod
    def method1():
        ## Try these 5 different commands below
        # raise ArithmeticError("ArithmeticError") # try these as well!
        # raise RuntimeError("RuntimeError")
        # raise AttributeError("Attribute error")
        div_by_zero = 12 / 0
        #div_by_two = 12 / 2  # No exception here!
        print("   at the end of method1")

    @staticmethod
    def method2():
        try:
            ExceptionDemo2.method1()
            print("   method1 called without any problems")
        except Exception as e: #Generic "Exception" is first now
            print("   in except Exception")
            #return # try with and without the return here!
        except ArithmeticError as e:
            print("   in except ArithmeticError")
            # return # try with and without the return here!
        except RuntimeError as e:
            print("   in except RuntimeError")
            # return # try with and without the return here!
        finally:
            print("   in the finally block")
            #return # try with and without the return here!

        print("   at the end of method2")


if __name__ == '__main__':

    print("Ready to call method2 ...")
    ExceptionDemo2.method2()
    print("After calling method2 ...")