class MyVeryOwnError(Exception):

    def __init__(self,msg):

        Exception.__init__(self,msg)

        #the __init__ constructor method calls the built-in Exception passing the msg parameter
        # Exception.__init__(self,msg) ensuring that msg is passed to the base class