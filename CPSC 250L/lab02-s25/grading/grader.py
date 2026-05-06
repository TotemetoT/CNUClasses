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
    print(f"  errors={num_errors} failures={num_failures} skipped={num_skipped}")
    return score

def score_style(files):
    """
    Calculate overall style points from list of files

    @param: files - list of source files to check
    @return: score 0 to 100
    """
    from grading.lint_test import lint_test
    total_style = 0
    print(f"\nRunning pylint checker ...")

    for file in files:
        print(f"\n  Running pylint for {file} ...")
        passed, style = lint_test(file)
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
    print(f"  Total style percentage = {style:6.2f}")
    return style

def grade_repo(args):

    """
    Customize this list of tests and files for each week
    """
    from tests import test_list_methods
    from tests import test_string_methods
    from tests import test_motion
    from tests import test_list_methods2
    lab_score = score_unit_tests([test_list_methods.TestListMethods,
                                  test_string_methods.TestStringMethods,
                                  test_motion.TestMotion,
                                  test_list_methods2.TestListMethods2])


    # Style checking
    if lab_score > 50.0:
        style_score = score_style(["src/list_methods.py", "src/string_methods.py",
                             "src/motion.py", "src/list_methods2.py"])
    else:
        print(" Ignore style points until you get at least 50% on correctness!")
        style_score = 0.0


    hw_score = 0.0  # No separate HW grade for lab
    final_grade = 0.30*style_score + 0.4*lab_score  # No separate HW grade for lab

    # For lab with 70 + 30 participation
    print(f"#Final grade = {final_grade:6.1f} of 70 + Participation (style={style_score:6.1f}, correctness={lab_score:6.1f})")

    if args:
        print(args)
        try:
            username = args[0]
            project_group = args[1]
            project = args[2]
            short_sha = args[3]
            commit_timestamp = args[4]
            pipeline_timestamp = args[5]
            # Assume remaining words are part of author tag
            author = " ".join(args[6:])

            # Plan to write this to a grading summary file
            suffix =  project_group[-12:]
            grade_string = f"{username},{project_group},{project},{final_grade:.1f},{style_score:.1f},{lab_score:.1f},{hw_score:.1f},{short_sha},{commit_timestamp},{pipeline_timestamp},{author}"
            if suffix == "-cpsc250-s23":
                # Must be student write to grading file for project
                print(grade_string) # Just print for now
            else:
                print(f"Unknown group suffix={suffix}: {args}")
                print(grade_string)

        except IndexError:
            print("   Cannot write to report as all arguments are not defined!")

    return final_grade

if __name__ == "__main__":

    # Usage:
    # PYTHONPATH=. python3 $UNITTEST $GITLAB_USER_LOGIN $CI_PROJECT_NAME $CI_COMMIT_SHORT_SHA $CI_COMMIT_TIMESTAMP $CI_PIPELINE_CREATED_AT $CI_COMMIT_AUTHOR
    # At least user is required!

    print(sys.argv)
    if grade_repo(sys.argv[1:]) < 65: # For lab with 70 + 30 participation
        sys.exit(-1)  # Some grading error to fix
