"""
Example test from https://justinnhli.com
"""
from contextlib import redirect_stdout
from io import StringIO
from os.path import expanduser, realpath, exists
import sys
from textwrap import indent, dedent

#from pylint.epylint import py_run
from pylint.lint import Run as PyLintRun

def lint_test(filepath):
    """Lint a python file.

    This function will use Pylint to check a Python file for code quality
    issues. If no issues are found, the function returns True. If any issues
    are found, the Pylint output is printed, and the function returns False.

    Parameters:
        filepath (str): The path to the file to lint.

    Returns: tuple of (bool, score)
        bool: True if the linter didn't find any issues, false otherwise.
        score: out of 10
    """
    file_path = realpath(expanduser(filepath))
    if not exists(file_path):
        print(f"Failed to find {filepath}")
        return False, -99.0

    passed = False
    # Redirect stdout and stderr
    pylint_stdout = StringIO()
    pylint_stderr = StringIO()
    # Save original stdout and stderr
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    try:

        # Redirect to StringIO objects
        sys.stdout = pylint_stdout
        sys.stderr = pylint_stderr
        command_string = [
            file_path,
            "--msg-template='Line {line}, column {column}: {msg}'",
            ]
        #print(f"Command string: <{command_string}>")
        exit_code = PyLintRun(command_string)

    except SystemExit as exc:
        exit_code = exc
    except Exception as exc:
        print("-----------")
        print("Exception: ", exc)
        print("-----------")
        print("-----------")
        self.fail(msg='failed to PyLint '+filepath)
    finally:
        # Restore original stdout and stderr
        sys.stdout = old_stdout
        sys.stderr = old_stderr


    actual_output = pylint_stdout.getvalue().strip()
    actual_output = actual_output.replace("\x1b[0m", "")  # Remove string coloring
    actual_output = actual_output.strip()
    actual_error  = pylint_stderr.getvalue().strip()

    lines = actual_output.splitlines()
    lint_passed = len(lines) == 2  # --- and rating
    lint_passed = lint_passed and (actual_error == '')

    if lint_passed:
        return True, 10.0
    else:
        transcript = '\n'.join(lines[1:])
        msg_str = dedent('''\n
There are some coding style issues with\n  {}:
{}
            ''').format(filepath, indent(transcript, '    '))

        print(msg_str)

        grade_string = lines[-1].split("(")[0]
        posn = len("Your code has been rated at ")
        #print(f" grade <{grade}> posn={posn}")
        try:
            grade_value = float(grade_string.strip()[posn:-3])
        except:
            grade_value = -99  # Flag issue processing the grade value

        if grade_value > 9.2:
            # Allow green check if above 92% for all files that are tested
            return True, grade_value
        else:
            return False, grade_value


if __name__ == '__main__':
    import sys
    for arg in sys.argv[1:]:
        passed, grade = lint_test(arg)
