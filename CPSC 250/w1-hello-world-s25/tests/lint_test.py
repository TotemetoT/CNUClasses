"""
Example test from https://justinnhli.com
"""
from contextlib import redirect_stdout
from io import StringIO
from os import chdir
from os.path import expanduser, realpath
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


def lint_test(filepath):
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
    actual_output = StringIO()
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
        except SystemExit:
            pass
    actual_output = actual_output.getvalue().strip()
    passed = (actual_output == '')
    if passed:
        return True, 10.0
    else:
        lines = actual_output.splitlines()
        transcript = '\n'.join(lines[1:])
        print(dedent('''
            There are some coding style issues:

            {}
        ''').strip().format(indent(transcript, '    ')))

        grade = lines[-1]
        posn = len("Your code has been rated at ")
        grade = float(lines[-1][posn:-3])
        #print("Grade: ",grade)
        return False, grade


if __name__ == '__main__':
    import sys
    for arg in sys.argv[1:]:
        passed, grade = lint_test(arg)
