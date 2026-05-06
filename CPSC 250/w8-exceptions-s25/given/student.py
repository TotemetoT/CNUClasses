"""
Use this to create Student class
 @author
 @version
"""
# pylint: disable-msg=C0103

from given.cnu_person import CNUPerson


class Student(CNUPerson):

    def __init__(self, first_name, last_name, id, gpa):

        # Call Person constructor to get all validation of names from Person
        CNUPerson.__init__(self, first_name, last_name, id)

        self.gpa = gpa

    def __str__(self):

        return "{} gpa({:.3f})".format(CNUPerson.__str__(self), self.gpa)

