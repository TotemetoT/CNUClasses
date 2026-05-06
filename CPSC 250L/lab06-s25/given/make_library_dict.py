"""
Create a dictionary to hold your library of books.

The dictionary should store a list of books for each type:
    "fiction", "nonfiction", and "textbook"

Use the `add_book` method to create the book dictionary,
and add the book to the proper dictionary.

Add at least three books of your choosing for each type,
and a total of at least 10 books to your library.

Then using proper loops, for each type, print
the title, author, year neatly formatted.

Clearly delineate each type of book by
drawing a line using `--------------` between each type
grouping, and label the type group.


@author Ryan Schatzberg
@version 2/25/2025

"""
# pylint: disable-msg=C0103

def add_book(title, author, year, book_list=None):
    """
    Creates a dictionary instance for each book with keys:
      title, author,  and year

    Make sure title and author are both non-empty strings

    Make sure year is an int

    otherwise print error message and return None if invalid data

    If valid book and book_list is valid list, then
    add the book dictionary to that list in place.

    :return: reference to the dictionary object or None
    """

    if not isinstance(year, int):
        print("Year must be int")
        return None
    if (not isinstance(title, str) or not isinstance(author, str) or
        len(author) == 0 or len(title) == 0):
        print("Both title and author must be non-empty strings")
        return None

    book = {"title": title, "author": author, "year": year}
    if isinstance(book_list, list):
        book_list.append(book)
    return book


if __name__ == '__main__':
    library = {"fiction": [], "nonfiction": [], "textbook": []}

    add_book("To Kill a Mockingbird", "Harper Lee", 1960, library["fiction"])
    add_book("1984", "George Orwell", 1949, library["fiction"])
    add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, library["fiction"])
    add_book("Moby Dick", "Herman Melville", 1851, library["fiction"])

    add_book("A Brief History of Time", "Stephen Hawking", 1988, library["nonfiction"])
    add_book("In Cold Blood", "Truman Capote", 1966, library["nonfiction"])
    add_book("The Diary of a Young Girl", "Anne Frank", 1947, library["nonfiction"])
    add_book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 2011, library["nonfiction"])

    add_book("Introduction to Algorithms", "Thomas H. Cormen", 2009, library["textbook"])
    add_book("Basic Economics", "Thomas Sowell", 2000, library["textbook"])
    add_book("Chemistry: The Central Science", "Theodore L. Brown", 2017, library["textbook"])
    add_book("Campbell Biology", "Lisa A. Urry", 2016, library["textbook"])

    for key, book_list in library.items():
        print(76*"-")
        print(33*"-" + f"{key:^10s}" + 33*"-")
        for book in book_list:
            print(f'{book["title"]:40s} {book["author"]:30s} {book["year"]:4d}')
        print()
