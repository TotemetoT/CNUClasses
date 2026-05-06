"""
Practice with lists and dictionaries


@author Ryan Schatzberg
@version 2.6.2025

"""
# pylint: disable-msg=C0103


def add_book(title, author, year, genre=None):
    """
    Creates a dictionary instance for each book with keys:
      title, author, and year

    Make sure title and author are both non-empty strings

    Make sure year is an int

    otherwise print error message and return None if invalid data

    If valid book and book_list is valid list, then
    add the book dictionary to that list in place.

    :return: reference to the dictionary object or None
    """
    if title and author != "":
        if type(title) and type(author) != str:
            print("Title and/or author isn't a string.")
            return None
    else:
        return None
    if type(genre) != list:
        return None
    if type(year) != int:
        print("Error, year is String type not Integer.")
        return None

    book_dict = {
        'title': title,
        'author': author,
        'year': year
    }
    genre.append(book_dict)
    return book_dict


if __name__ == '__main__':
    # This code provided to help you test.
    # Nothing required to change below this line, but you can
    # modify as you like.

    print(" Example usage of add_book :")

    # Get the stock dictionary as defined in README
    book_list = []
    book = add_book("The Lord of the Rings", "J.R.R. Tolkien", 1954, book_list)

    assert book is not None, "must return valid dictionary"
    assert isinstance(book, dict), "must be a dictionary"

    print("book in library: ", book is book_list[0]) # better be same instance
    for book_ in book_list:
        print(book_)

    book = add_book("The Lord of the Rings", "J.R.R. Tolkien", "not a year", book_list)
    assert book is None, "invalid year"
