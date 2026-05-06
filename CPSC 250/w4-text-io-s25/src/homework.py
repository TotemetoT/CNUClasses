"""

Homework for Week 4

@author <your name here>
"""

# Q1
def login_from_name(students):
    """
    Given a list of strings "last, first"
    Return a list of usernames.
    Usernames must be the first character of the user's first name,
    followed by the first four letters of their last name,
    followed by 21, all in lowercase
       e.g. given ["Chris, Captain", "Smith, John"]
            return ["cchri21", "jsmit21"]

    If the students is None, then return None
    If empty list, then return a valid empty list

    Note:
          The students list input argument will only contain valid strings in "Last, First" format,
          but it might be empty or None

    :param students: list of student names in "Last, First" format
    :return: list of student logins or None
    """
    if not students or students == []:
        return None
    username_list = []
    for student in students:
        first = ""
        last = ""
        for i in range(len(student)):
            if student[i] == ",":
                last = student[:i-1].lower()
                if len(last) >= 4:
                    last = last[:4]
                first = student[i+2].lower()
        username_list.append(f'{first}{last}21')
    return username_list

# Q2
def dictionary_from_names(universities):
    """
    Given a list of university names,
    return a dictionary with
    the initials of the university as the key and the name as the value.

    e.g. given ["Christopher Newport University",  "Virginia Tech", "Virginia Commonwealth University", "George Washington University"]
         return {"CNU" : "Christopher Newport University",
                 "VT"  : "Virginia Tech",
                 "VCU" : "Virginia Commonwealth University",
                 "GWU" : "George Washington University"}

    Note: You can assume a properly formatted list is passed as input

    :param universities: a list of university names
    :return: a dictionary containing abbreviations and university names as key:value pairs
    """
    school_dict = {}
    for school in universities:
        temp = ""
        for char in school:
            if char != " ":
                if char.isupper():
                    temp += char
        school_dict[temp] = school
    return school_dict


if __name__ == '__main__':
    print("Use this area to debug your programs if needed")
    # Hint: Use the information given in the docstrings to write simple tests to debug your code


    print("#Q1")
    print("Actual:  ", login_from_name(["Chris, Captain", "Smith, John", "Trible, Paul"]))
    print("Expected:", ['cchri21', 'jsmit21'])

    sample_universities = ["Christopher Newport University", "Virginia Commonwealth University",
                           "Virginia Polytechnic Institute", "Carnegie Mellon University"]

    print("#Q2")
    formatted_strings = dictionary_from_names(sample_universities)
    print("Actual:  ", formatted_strings)
    print("Expected:", {"CNU" : "Christopher Newport University", "VCU" : "Virginia Commonwealth University",
                       "VPI" : "Virginia Polytechnic Institute", "CMU":"Carnegie Mellon University"})
