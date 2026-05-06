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

#from pylint.epylint import py_run
from pylint.lint import Run as PyLintRun


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
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        try:
            command_string = [
                file_path,
                "--msg-template='Line {line}, column {column}: {msg}'",
                ]
            #print(f"Command string: <{command_string}>")
            PyLintRun(command_string)
        except SystemExit:
            pass
        except Exception as exc:
            print("-----------")
            print("Exception: ", exc)
            print("-----------")
            print("-----------")
            self.fail(msg='failed to PyLint '+filepath)
        pylint_stdout = sys.stdout.getvalue()
        pylint_stderr = sys.stderr.getvalue()
        sys.stdout = original_stdout
        sys.stderr = original_stderr


        actual_output = pylint_stdout.strip()
        actual_output = actual_output.replace("\x1b[0m", "")  # Remove string coloring
        actual_output = actual_output.strip()
        actual_error  = pylint_stderr.strip()
        lines = actual_output.splitlines()
        lint_passed = len(lines) == 2  # --- and rating
        passed = lint_passed and (actual_error == '')

        #print("-----------")
        #print(f"pylint_stdout: <{actual_output}>")
        #print(f"pylint_stderr: <{actual_error}>")
        #print("passed=",passed, lint_passed)
        #print("===============")

        if passed:
            return True
        else:
            transcript = '\n'.join(actual_output.splitlines()[1:])
            msg_str = dedent('''\n
There are some coding style issues with\n  {}:
{}
            ''').format(filepath, indent(transcript, '    '))
            #print(msg_str)
            self.fail(msg_str)
            return False

    def test_add_book(self):
        self.lint_test(self.__path+"add_book.py")

    def test_make_library(self):
        self.lint_test(self.__path+"make_library.py")


if __name__ == '__main__':
    unittest.main()
