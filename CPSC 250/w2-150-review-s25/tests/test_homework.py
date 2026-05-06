"""
Test for HW 4 - Do this individually

Put this in source so we can check the unit tests that students write for the other values.


"""
import unittest
from src import homework

class TestHomework(unittest.TestCase):
    """
        Test Class for homework.py
    """

    def setUp(self):
        #These names were randomly generated, they are not based on real student names: https://homepage.net/name_generator/
        self._names = ["Anna Welch","Victor Miller","Isaac Paige","Carl Wilkins","Elizabeth Randall","Karen Pullman","Sebastian Paterson","Ava Powell","Keith Fisher","Nicholas Lawrence"]
        self._emails = ['anna.welch.19@cnu.edu', 'victor.miller.19@cnu.edu', 'isaac.paige.19@cnu.edu', 'carl.wilkins.19@cnu.edu', 'elizabeth.randall.19@cnu.edu', 'karen.pullman.19@cnu.edu', 'sebastian.paterson.19@cnu.edu', 'ava.powell.19@cnu.edu', 'keith.fisher.19@cnu.edu', 'nicholas.lawrence.19@cnu.edu']
        self._usernames = ['anna.welch.19', 'victor.miller.19', 'isaac.paige.19', 'carl.wilkins.19', 'elizabeth.randall.19', 'karen.pullman.19', 'sebastian.paterson.19', 'ava.powell.19', 'keith.fisher.19', 'nicholas.lawrence.19']
        self._greetings = ['Dear Anna Welch,', 'Dear Victor Miller,', 'Dear Isaac Paige,', 'Dear Carl Wilkins,', 'Dear Elizabeth Randall,', 'Dear Karen Pullman,', 'Dear Sebastian Paterson,', 'Dear Ava Powell,', 'Dear Keith Fisher,', 'Dear Nicholas Lawrence,']

    def test_hw4_email_year(self):
        addresses =  homework.create_email_addresses(self._names)
        for address in addresses:
            self.assertTrue(address.find(".19") >= 0, msg="For this example we are assuming everyone matriculated in 2019, so the year would be 19")

    def test_hw4_email_cnudomain(self):
        addresses = homework.create_email_addresses(self._names)
        for address in addresses:
            self.assertTrue(address[-8:] == "@cnu.edu", msg="The email domain should be cnu.edu")

    def test_hw4_email_lowercasenames(self):
        addresses = homework.create_email_addresses(self._names)
        for address in addresses:
            name = address.split("@")[0]
            self.assertTrue(name == name.lower(), msg="The first and last names in the email address should be lower case")

    def test_hw4_email_exact(self):
        addresses = homework.create_email_addresses(self._names)
        self.assertTrue(addresses == self._emails,msg="The email addresses that you created are not an exact match to the solution")

    def test_hw4_emailheader_dear(self):
        headers = homework.create_email_headers(self._usernames)
        for header in headers:
            self.assertTrue(header[:5] == "Dear ", msg="The email header should start with Dear ")

    def test_hw4_emailheader_comma(self):
        headers = homework.create_email_headers(self._usernames)
        for header in headers:
            self.assertTrue(header[-1:] == ",", msg="The email header should end with a comma!")

    def test_hw4_emailheader_exact(self):
        headers = homework.create_email_headers(self._usernames)
        self.assertTrue(headers == self._greetings,msg="The email greetings that you created are not an exact match to the solution")

    def test_hw4_split_email_contains_at_symbol(self):
        usernames = homework.split_emails(self._emails)
        for username in usernames:
            self.assertTrue(username.find("@") == -1, msg="Username contains @ symbol, which it should not.")

    def test_hw4_split_email_period_separated(self):
        usernames = homework.split_emails(self._emails)
        for username in usernames:
            self.assertTrue(len(username.split(".")) > 0, msg="Username should be period separated. Return a username in the format first.last.YY")

    def test_hw4_split_email_exact(self):
        usernames = homework.split_emails(self._emails)
        self.assertTrue(usernames == self._usernames,
                        msg="The usernames that you created are not an exact match to the solution, check the instructions and other test cases")




if __name__ == '__main__':
    unittest.main()
