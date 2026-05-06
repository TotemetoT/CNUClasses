"""
We define a comboSuite to combine multiple test files into a single test file
to execute.

Students - DO NOT MODIFY THIS FILE!

"""
import unittest
import sys

def score_unit_tests(tests):
    """
    Run all tests from list of test classes

    @param: tests - list of class definitions for tests
    @return: score 0 to 100
    """
    print("   score unit tests ...", flush=True)
    suiteList = []
    for test in tests:
        suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test))

    comboSuite = unittest.TestSuite(suiteList)
    result = unittest.TextTestRunner(verbosity=1).run(comboSuite)

    num_errors = len(result.errors)
    num_failures = len(result.failures)
    num_skipped = len(result.skipped)
    num_tests = result.testsRun

    # Correctness score percentage
    score = 100.0*(num_tests - (num_errors+num_failures+num_skipped))/num_tests
    print(f" correctness = {score:6.2f}% : Tests={num_tests} ", end="")
    print(f"    errors={num_errors} failures={num_failures} skipped={num_skipped}", flush=True)
    return score

def score_style(files):
    """
    Calculate overall style points from list of files

    @param: files - list of source files to check
    @return: score 0 to 100
    """
    print(f"\nRunning pylint checker ...", flush=True)
    try:
        from grading.lint_test import lint_test
    except Exception as exc:
        print(exc)
        print(" cannot run lint test!")
        return 0

    total_style = 0

    for file in files:
        print(f"\n  Running pylint for {file} ...")
        try:
            passed, style = lint_test(file)
        except Exception as exc:
            print(exc, flush=True)
            score = 0

        total_style += style
        print(20*"-")

    # Convert to percentage points
    if len(files) > 0:
        style = total_style*(10./len(files)) # total style in percentage
        if style < 0.0:
            style = 0.0
    else:
        style = 0.0

    print(30*"=")
    print(f"  Total style percentage = {style:6.2f}", flush=True)
    return style

def grade_repo():
    """
    Define the project grader for specific files
    """

    """
    Customize this list of tests and files for each week
    """
    from tests import test_list_methods
    from tests import test_homework

    print("Grading repo ...", flush=True)
    weekly_score = score_unit_tests([test_list_methods.TestListMethods])

    hw_score = score_unit_tests([test_homework.TestHomework])

    # Style checking
    if weekly_score > 50.0 and hw_score > 50.0:
        style_score = score_style(["src/list_methods.py",
                                   "src/homework.py"])
    else:
        print(" Ignore style points until you get at least 50% on correctness!")
        style_score = 0.0

    final_grade = 0.10*style_score + 0.45*weekly_score + 0.45*hw_score
    print(f"#Final grade = {final_grade:6.1f} ")
    return final_grade

if __name__ == "__main__":
    if grade_repo() < 92:
        # Give an X on Gitlab CI page
        sys.exit(-1)  # Some grading error to fix
