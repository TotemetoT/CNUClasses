"""
Based on lint_test.py from https://justinnhli.com
"""

import unittest
import sys

from contextlib import redirect_stdout
from io import StringIO
#from os import chdir
from os.path import exists, expanduser, realpath
from textwrap import indent, dedent

# from pylint.epylint import py_run
from pylint.lint import Run as PyLintRun

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
    """
    Test class for our Lint checker
    """
    def setUp(self):
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

        file_path = realpath(expanduser(filepath))
        if not exists(file_path):
            print(f"Failed to find {filepath}")
            self.fail(msg='failed to PyLint '+filepath)

        passed = False
        try:
            command_string = [
                file_path,
                "--msg-template='Line {line}, column {column}: {msg}'",
                ]
            # print(f"Command string: <{command_string}>")
            (pylint_stdout, pylint_stderr) = PyLintRun(command_string)  # , return_std=True)

        except SystemExit as exc:
            #  print(f"SysExit: {exc}", flush=True)
            return True

        except Exception as exc:
            print("-----------")
            print("Exception: ", exc)
            print("-----------")
            print("-----------")
            self.fail(msg='failed to PyLint '+filepath)


        actual_output = pylint_stdout.read().strip()
        actual_output = actual_output.replace("\x1b[0m", "")  # Remove string coloring
        actual_output = actual_output.strip()
        actual_error  = pylint_stderr.read().strip()
        lines = actual_output.splitlines()
        lint_passed = len(lines) == 2  # --- and rating
        passed = lint_passed and (actual_error == '')

        #print("-----------")
        #print(f"pylint_stdout: <{actual_output}>")
        #print(f"pylint_stderr: <{actual_error}>")
        #print("passed=",passed, lint_passed)
        #print("===============")

        if passed:
            # No problems detected!
            return True
        else:
            transcript = '\n'.join(actual_output.splitlines()[1:])
            msg_str = dedent('''\n
There are some coding style issues with\n  {}:
{}
            ''').format(filepath, indent(transcript, '    '))
            #print(msg_str)

            grade_string = lines[-1].split("(")[0]
            posn = len("Your code has been rated at ")
            #print(f" grade <{grade}> posn={posn}")
            try:
                grade_value = float(grade_string.strip()[posn:-3])
            except:
                grade_value = -99  # Flag issue processing the grade value

            if grade_value > 9.0:
                print(f"Some problems, rating of {grade_value}, but we'll still give you a check mark for 9 of 10!")
                print(msg_str)
                return False
            else:
                self.fail(msg_str)

    def test_string_methods(self):
        """ Call linter"""
        self.lint_test(self.__path+"string_methods.py")

    def test_list_methods(self):
        """ Call linter"""
        self.lint_test(self.__path+"list_methods.py")

    def test_list_methods2(self):
        """ Call linter"""
        self.lint_test(self.__path+"list_methods2.py")

    def test_motion(self):
        """ Call linter"""
        self.lint_test(self.__path+"motion.py")


if __name__ == '__main__':
    unittest.main()
