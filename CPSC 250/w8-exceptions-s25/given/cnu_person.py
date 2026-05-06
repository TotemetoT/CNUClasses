"""
Use this to create CNUPerson class
 @author
 @version
"""
# pylint: disable-msg=C0103

from given.person import Person


class CNUPerson(Person):

    def __init__(self, first_name,last_name, id):

        # Call Person constructor to get all validation of names from Person
        Person.__init__(self, first_name, last_name)

        self.id = id

    def __str__(self):

        return "{} ({})".format(Person.__str__(self), self.id)
