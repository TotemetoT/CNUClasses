import os
import unittest
import subprocess
import sys

class TestSayIt(unittest.TestCase):

    def setUp(self):
        self.__timeout = 2

        # Check to see if we are running in the tests directory, if so set the current directory to the parent directory
        if(os.path.basename(os.getcwd()) == "tests"):
            # Change the current directory to the parent directory
            os.chdir("..")

        self.__path = "src/"



    def test_if_main(self):

        expected = "Hello World!"
        try:
            if(is_windows()):
                proc = subprocess.Popen([sys.executable, self.__path + "hello_world.py"], stdout=subprocess.PIPE, shell=True)
                (output, error) = proc.communicate(timeout=self.__timeout)
            else:
                proc = subprocess.Popen(["python3 "+self.__path+"hello_world.py"], stdout=subprocess.PIPE, shell=True)
                (output, error) = proc.communicate(timeout=self.__timeout)
        except TimeoutError:
            self.fail(msg='python hello_world.py timed out.')

        output_str = output.decode('utf-8').rstrip() # Convert bytes and remove the newline added by print
        self.assertEqual(expected, output_str,msg="hello_world.py output is incorrect: Expected({}) Actual ({})".format(expected, output_str))

    def test_say_it(self):
        expected = "Hello World!"
        try:
            if (is_windows()):
                proc = subprocess.Popen([sys.executable, self.__path + "say_it.py"], stdout=subprocess.PIPE, shell=True)
                (output, error) = proc.communicate(timeout=self.__timeout)
            else:
                proc = subprocess.Popen(["python3 " + self.__path + "say_it.py"], stdout=subprocess.PIPE, shell=True)
                (output, error) = proc.communicate(timeout=self.__timeout)
        except TimeoutError:
            self.fail(msg='python hello_world.py timed out.')

        output_str = output.decode('utf-8').rstrip() # Convert bytes and remove the newline added by print
        self.assertEqual(expected, output_str,msg="say_it.py output is incorrect: Expected({}) Actual ({})".format(expected, output_str))

def is_windows():
    return os.name == 'nt'

if __name__ == '__main__':
    unittest.main()
