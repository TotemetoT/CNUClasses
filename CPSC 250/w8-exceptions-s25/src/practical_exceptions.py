from given.person import Person
from given.cnu_person import CNUPerson
from given.student import Student
import os


def convert_data(sample_user_input):
    """
    Given a list of simulated user input that are supposed to be numbers return a list of integers.
    If the value is unable to be convert it to an integer do not add it to the list of integers.

        Note: You should be catching exceptions here! Do not try to check the type!

    :param sample_user_input: A list
    :return: a list of integers
    """
    integers = []
    for item in sample_user_input:
        try:
            integers.append(int(item))
        except ValueError:
            pass
    return integers


def safe_open_text(file_path):
    """
    Given a filepath return an opened file handle in write text mode or raise a FileExistsError exception if the file exists!

    Note: Use the os module to check to see if the file exists!

    :param file_path:
    :return: file
    """
    if os.path.exists(file_path):
        raise FileExistsError(f"The file '{file_path}' already exists.")
    return open(file_path, "w")


def read_in_people(file_path):
    """
    Using the Person, CNUPerson and Student classes in the given folder,
    we will be opening a csv text file and creating instances based upon the input data.
    We must be prepared to handle exceptions that may arise when working with these classes.

    Hint:
         - You will need to use the try and except blocks to handle the exceptions.
         - You can use the number of columns in the csv file to determine which class to use.

    Note:
    The Person, CNUPerson and Student classes in the given folder are slightly different than the ones in that
    we have used in the past so please pay attention to the differences! In particular, the Person class requires valid first and last names.

    :param file_path
    :return: a list of instances of Person, CNUPerson, and Student
    """
    people = []
    try:
        with open(file_path, encoding='utf-8') as file:
            for line in file:
                row = line.strip().split(",")
                try:
                    if len(row) == 2:
                        people.append(Person(row[0], row[1]))  # First name, Last name
                    elif len(row) == 3:
                        people.append(CNUPerson(row[0], row[1], row[2]))  # First name, Last name, ID
                    elif len(row) == 4:
                        people.append(Student(row[0], row[1], row[2], row[3]))  # First name, Last name, ID, Major
                    else:
                        raise ValueError(f"Invalid number of fields in line: {line}")
                except Exception as e:
                    print(f"Error processing line {line}: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return people


if __name__ == '__main__':
    sample_data = [1, 5, 7, "9", "eleven"]
    expected = [1, 5, 7, 9]
    actual = convert_data(sample_data)
    print("Expected:", expected)
    print("Actual:", actual)

    try:
        file = safe_open_text(os.path.join("data", "safe_open_test_file.txt"))
        file.close()    # Remember, always close the file!
    except FileExistsError as e:
        print(e)
    except Exception:
        print("Something went wrong, you raised the wrong exception?")

    # Read in the people from the csv file.
    people = read_in_people(os.path.join("data", "people.txt"))
    for person in people:
        print(person)

    # Read in the people from the csv file. This time survey_data.txt has missing data that will raise an exception (that you should handle).
    people = read_in_people(os.path.join("data", "survey_data.txt"))
    for person in people:
        print(person)