"""
Use this to create Person class
 @author
 @version
"""
# pylint: disable-msg=C0103


class Person:

    def __init__(self, first_name, last_name):
        if first_name == "":
            raise Exception(" Must have valid first name")

        if last_name == "":
            raise Exception(" Must have valid last name")

        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __eq__(self, other):
        # print("Calling equality check with {} == {}".format(id(self), id(other)))
        if self.last_name != other.last_name:
            return False
        if self.first_name != other.first_name:
            return False
        return True

    def __lt__(self, other):
        if not isinstance(other, Person):
            print(str(other) + " is not a Person instance")
            return False

        if self.last_name < other.last_name:
            return True
        elif self.last_name == other.last_name:
            if self.first_name < other.first_name:
                return True
        return False
