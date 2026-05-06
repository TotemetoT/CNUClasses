"""
Based on lint_test.py from https://justinnhli.com
"""
import os
import unittest
import sys

from contextlib import redirect_stdout
from io import StringIO
#from os import chdir
from os.path import exists, expanduser, realpath
from textwrap import indent, dedent

from pylint.lint import Run as lint

# lint checks taken from
# https://pylint.readthedocs.io/en/latest/technical_reference/features.html#python3-checker-messages
LINT_CHECKS = [
    # redundancy
    'duplicate-code',
    # conventions
    'singleton-comparison',
    'line-too-long',
    'trailing-whitespace',
    'superfluous-parens',
    'bad-whitespace',
    # warnings
    'invalid-name',
    'unreachable',
    'dangerous-default-value',
    'pointless-statement',
    'expression-not-assigned',
    'unnecessary-pass',
    'useless-else-on-loop',
    'exec-used',
    'eval-used',
    'using-constant-test',
    'unnecessary-semicolon',
    'bad-indentation',
    'mixed-indentation',
    'reimported',
    'global-statement',
    'unused-import',
    'unused-variable',
    'unused-argument',
    # errors
    'syntax-error',
    'function-redefined',
    'not-in-loop',
    'return-outside-function',
    'nonexistent-operator',
    'duplicate-argument-name',
    'used-before-assignment',
    'undefined-variable',
    'assignment-from-none',
]



class TestPyLint(unittest.TestCase):

    def setUp(self):
        self.__timeout = 2

        # Check to see if we are running in the tests directory, if so set the current directory to the parent directory
        if (os.path.basename(os.getcwd()) == "tests"):
            # Change the current directory to the parent directory
            os.chdir("..")

        self.__path = "src/"

    def lint_test(self, filepath):
        """Lint a python file.

        This function will use Pylint to check a Python file for code quality
        issues. If no issues are found, the function returns True. If any issues
        are found, the Pylint output is printed, and the function returns False.

        Parameters:
            filepath (str): The path to the file to lint.

        Returns:
            bool: True if the linter didn't find any issues, false otherwise.
        """

        realpath(expanduser(filepath))
        if not exists(filepath):
            self.fail(msg='failed to PyLint ' + filepath+" - File does not exist!")

        actual_output = StringIO()
        passed = False
        with redirect_stdout(actual_output):
            try:
                lint([
                    filepath,
                    "--msg-template='Line {line}, column {column}: {msg}'",
                    '--disable=all',
                    '--enable=' + ','.join(sorted(LINT_CHECKS)),
                    '--max-line-length=150',
                    '--persistent=n',
                ])
            except SystemExit as e:
                passed = str(e) == '0'
                pass

            except Exception as e:
                print("-----------")
                print("Exception: ", e)
                print("-----------")
                print("-----------")
                self.fail(msg='failed to PyLint '+filepath)


        actual_output = actual_output.getvalue().strip()
        passed = passed or (actual_output == '')

        #print("-----------")
        #print("Actual Output:", actual_output)
        #print("passed=",passed)f
        #print("===============")
        sys.stdout.flush()
        if passed:
            return True
        else:
            transcript = '\n'.join(actual_output.splitlines()[1:])
            msg_str = dedent('''
                There are some coding style issues:

                {}
            ''').strip().format(indent(transcript, '    '))
            #print(msg_str)
            self.fail(msg=msg_str)


    def test_hello_world(self):
        self.lint_test(self.__path+"hello_world.py")

    def test_say_it(self):
        self.lint_test(self.__path+"say_it.py")

    def test_hw3(self):
        self.lint_test(self.__path+"homework.py")


    #def test_bad_code(self):
    #    self.lint_test("given/bad_code.py")

if __name__ == '__main__':
    unittest.main()
