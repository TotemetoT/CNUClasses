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

def grade_repo(args):
    """
    Define the project grader for specific files
    """

    """
    Customize this list of tests and files for each week
    """

    print("Grading repo ...", flush=True)
    from tests import test_string_methods
    from tests import test_grocery_stock
    from tests import test_grocery_shop_total
    from tests import test_grocery_shop_out_of_stock
    from tests import test_grocery_shop_receipt
    lab_score = score_unit_tests([test_string_methods.TestStringMethods,
                                  test_grocery_stock.TestStock,
                                  test_grocery_shop_total.TestGroceryTotal,
                                  test_grocery_shop_out_of_stock.TestGroceryOutOfStock,
                                  test_grocery_shop_receipt.TestGroceryReceipt])


    # Style checking
    if lab_score > 50.0:
        try:
            style_score = score_style(["src/string_methods.py", "src/grocery_store.py"])
        except Exception as exc:
            print(exc, flush=True)
            style_score = 0.0
    else:
        print(" Ignore style points until you get at least 50% on correctness!", flush=True)
        style_score = 0.0


    hw_score = 0.0  # No separate HW grade for lab
    final_grade = 0.30*style_score + 0.4*lab_score  # No separate HW grade for lab

    # For lab with 70 + 30 participation
    print(f"#Final grade = {final_grade:6.1f} of 70 + Participation (style={style_score:6.1f}, correctness={lab_score:6.1f})", flush=True)

    return final_grade

if __name__ == "__main__":

    # Usage:
    # PYTHONPATH=. python3 $UNITTEST $GITLAB_USER_LOGIN $CI_PROJECT_NAME $CI_COMMIT_SHORT_SHA $CI_COMMIT_TIMESTAMP $CI_PIPELINE_CREATED_AT $CI_COMMIT_AUTHOR
    # At least user is required!
    #print(sys.argv)
    if grade_repo(sys.argv[1:]) < 65: # For lab with 70 + 30 participation
        # Give an X on Gitlab CI page
        sys.exit(-1)  # Some grading error to fix
