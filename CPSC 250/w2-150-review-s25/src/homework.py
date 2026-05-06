"""
Homework - Do this individually

@author Ryan Schatzberg
@version 1/25/2025
"""


def split_emails(list_of_emails):
    """
    This function should take in a list of email addresses and split them
    by the "@" symbol and return a new list of usernames

    :param list_of_emails: a list of email addresses formatted like first.last.YY@domain.edu
    :return: usernames: List of usernames formatted like first.last.YY
    """
    temp_list = []
    for i in range(len(list_of_emails)):
        for j in range(len(list_of_emails[i])):
            if list_of_emails[i][j] == '@':
                temp_list.append(list_of_emails[i][:j])
    return temp_list


def create_email_headers(usernames):
    """
    This function should take in a list of usernames in the first.last.YY format
    and return a list of email greetings.
    In order to properly create an email greeting you will need to split the
    username into the first and last name components.
    Note: You should capitalize the first letter in each name!
    The format for the greeting should be "Dear Firstname Lastname,"
    (Don't forget the comma!)

    :param usernames: usernames: a list of usernames formatted like first.last.YY
    :return: email_headers: a list of email headers formatted like "Dear Christopher Newport,"
    """
    email_list = []
    for i in range(len(usernames)):
        temp_list = []
        count = 0
        for j in range(len(usernames[i])):
            if count == 0:
                if usernames[i][j] == '.':
                    temp_list.append(usernames[i][:j].capitalize())
                    num = j + 1
                    count += 1
            elif count == 1:
                if usernames[i][j] == '.':
                    temp_list.append(usernames[i][num:j].capitalize())
                    count += 1
                    email_list.append(temp_list.copy())
            else:
                pass
    headers = []
    for i in range(len(email_list)):
        headers.append(f'Dear {email_list[i][0]} {email_list[i][1]},')
    return headers




def create_email_addresses(names):
    """
    This function will take in a list of names and will return email addresses
    with first.last.19@cnu.edu formatting.
    Note: Make sure to use the .lower() function to change the first and
     last names to all lower case!

    :param names: a list of names where the first and last name are space
    separated like example: "Bilbo Baggins"
    :return: email_addresses: a list of properly formatted
                                    email addresses first.last.19@cnu.edu
    """
    emails = []
    name = []
    for i in range(len(names)):
        count = 0
        temp_list = []
        for j in range(len(names[i])):
            if count == 0:
                if names[i][j] == ' ':
                    temp_list.append(names[i][:j].lower())
                    num = j+1
                    count += 1
            elif count == 1:
                temp_list.append(names[i][num:].lower())
                name.append(temp_list.copy())
                count += 1
            else:
                pass
    for i in range(len(name)):
        emails.append(f'{name[i][0]}.{name[i][1]}.19@cnu.edu')
    return emails


if __name__ == "__main__":

    # Constant uses UPPER_CASE style
    NAMES = ["Anna Welch", "Victor Miller", "Isaac Paige", "Carl Wilkins",
             "Elizabeth Randall", "Karen Pullman", "Sebastian Paterson",
             "Ava Powell", "Keith Fisher", "Nicholas Lawrence"]
    print(create_email_headers(split_emails(create_email_addresses(NAMES))))
    ADDRESSES = create_email_addresses(NAMES) # this is constant so UPPER_CASE style
    for address in ADDRESSES:
        print(address[-8:])
    print(ADDRESSES)
