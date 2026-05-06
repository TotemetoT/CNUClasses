# """
# Use this to create Person class
#  @author
#  @version
# """
# # pylint: disable-msg=C0103
#
#
# class Person:
#     """
#     Class to handle Person names with an optional second last name
#     https://webpages.uncc.edu/mperez19/twolastnames.html
#     https://diverseeducation.com/article/198351
#     """
#
#
#     def __init__(self, first_name, middle_name, last_name, second_last_name=None):
#         #@TODO - validate that first and last are valid strings
#         #   with (len > 1) and valid alphabetic character
#         # See https://docs.python.org/3/library/stdtypes.html  isalpha()
#         # (Our person won't accept Elon's kid's name,
#         #    but CNU can deal with that later)
#         #    https://www.bbc.com/news/world-us-canada-52557291
#         #
#         #  raise a TypeError or ValueError if invalid
#         #     ("Foreshadowing, your clue to quality literature!")
#
#         #@TODO - validate middle name is string, but can be empty!
#
#         # https://webpages.uncc.edu/mperez19/twolastnames.html
#         #@TODO - Validate that second last name is string or None
#         # Convert empty string to None type to standardize handling
#
#         if first_name =='':
#             raise Exception("Must have valid first name")
#         if last_name == '':
#             raise Exception("Must have valid last name")
#         if second_last_name == '':
#             second_last_name = None
#
#         self.first_name = first_name
#         self.middle_name = middle_name
#         self.last_name = last_name
#         self.second_last_name = second_last_name
#     def __str__(self):
#         if self.second_last_name is None:
#             return "{} {} {} ".format(self.first_name,self.middle_name,self.last_name)
#         else:
#             return "{} {} {} {} ".format(self.first_name,self.middle_name,self.last_name,self.second_last_name)
#
#     def __eq__(self,other):
#         if self.last_name != other.last_name:
#             return False
#         if self.second_last_name != other.second_last_name:
#             return False
#         if self.first_name != other.first_name:
#             return False
#         if self.middle_name != other.middle_name:
#             return False
#
#         return True
#
#     def __lt__(self,other):
#         if not isinstance(other,Person):
#             print(str(other) + " is not a Person instance")
#
#         if self.last_name < other.last_name:
#             return True
#         if self.last_name == other.last_name:
#             if self.second_last_name == other.second_last_name:
#                 if self.first_name == other.first_name:
#                     # if self.middle_name == other.middle_name:
#                     return True
#                 elif self.first_name != other.first_name:
#                     return self.middle_name < other.middle_name
#             elif self.second_last_name is not None and other.second_last_name is not None:
#                 if self.second_last_name < other.second_last_name:
#                     return True
#                 elif self.second_last_name is None and other.second_last_name is not None:
#                     return True
#         return False

"""
Use this to create Person class
 @author
 @version
"""
# pylint: disable-msg=C0103


class Person:
    """
    Class to handle Person names with an optional second last name
    https://webpages.uncc.edu/mperez19/twolastnames.html
    https://diverseeducation.com/article/198351
    """


    def __init__(self, first_name, middle_name, last_name, second_last_name=None):
        #@TODO - validate that first and last are valid strings
        #   with (len > 1) and valid alphabetic character
        # See https://docs.python.org/3/library/stdtypes.html  isalpha()
        # (Our person won't accept Elon's kid's name,
        #    but CNU can deal with that later)
        #    https://www.bbc.com/news/world-us-canada-52557291
        #
        #  raise a TypeError or ValueError if invalid
        #     ("Foreshadowing, your clue to quality literature!")

        #@TODO - validate middle name is string, but can be empty!

        # https://webpages.uncc.edu/mperez19/twolastnames.html
        #@TODO - Validate that second last name is string or None
        # Convert empty string to None type to standardize handling

        if first_name == "":
            raise Exception(" Must have valid first name")

        if last_name == "":
            raise Exception(" Must have valid last name")

        if second_last_name == "":
            second_last_name = None

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.second_last_name = second_last_name

    def __str__(self):

        if self.second_last_name is None:
            return "{} {} {}".format(self.first_name, self.middle_name,
                                     self.last_name)
        else:
            return "{} {} {}-{}".format(self.first_name, self.middle_name,
                                        self.last_name, self.second_last_name)

    def __eq__(self, other):
        # print("Calling equality check with {} == {}".format(id(self), id(other)))
        if self.last_name != other.last_name:
            return False
        if self.second_last_name != other.second_last_name:
            return False
        if self.first_name != other.first_name:
            return False
        if self.middle_name != other.middle_name:
            return False
        # Everything checks out, must be true!
        return True

    def __lt__(self, other):
        if not isinstance(other, Person):
            print(str(other) + " is not a Person instance")
            return NotImplemented

        if self.last_name != other.last_name:
            return self.last_name < other.last_name

        if self.second_last_name is None and other.second_last_name is not None:
            return True
        if self.second_last_name is not None and other.second_last_name is None:
            return False
        if self.second_last_name != other.second_last_name:
            return self.second_last_name < other.second_last_name

        if self.first_name != other.first_name:
            return self.first_name < other.first_name

        return self.middle_name < other.middle_name  # Ensures middle name is compared last
