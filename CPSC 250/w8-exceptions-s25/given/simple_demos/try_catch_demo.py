try:
    # execute some code
    x = 5
    y = 0
    z = x / y
except Exception as e:
    print("handling the exception, e = ", e)
    # do something to handle the exception

finally:
    print("do some cleanup")
    # do some clean up
