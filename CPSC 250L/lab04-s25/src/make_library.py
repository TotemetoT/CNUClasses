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
@version 2.6.2025

"""
from add_book import add_book
fiction, nonfiction, textbook = [],[],[]
library = {'fiction': fiction,
           'nonfiction': nonfiction,
           'textbook': textbook}
add_book("Harry Potter 1", "J.R.R. Tolkien", 1954, fiction)
add_book("Harry Potter 2", "J.R.R. Tolkien", 1954, fiction)
add_book("Harry Potter 2.5", "J.R.R. Tolkien", 1954, fiction)
add_book("Harry Potter 4", "J.R.R. Tolkien", 1954, fiction)
add_book("Real Life Harry Potter", "J.R.R. Tolkien", 1954, nonfiction)
add_book('In Cold Blood', 'J.R.R. Tolkien', 1954, nonfiction)
add_book('That nonfiction journal', 'J.R.R. Tolkien', 1954, nonfiction)
add_book('Basic Economics', 'J.R.R. Tolkien', 1954, textbook)
add_book('Stats...', 'J.R.R. Tolkien', 1954, textbook)
add_book('Programming for data stuff', 'J.R.R. Tolkien', 1954, textbook)
tring = ''
dash = '---------------------------------------------------------------'
dash2 = '----------------------------'
tring += f'{dash}{dash2}'
I2 = 0
for key in library:
    tring += f'\n{key.center(91, "-")}\n'
    value = library[key]
    for i in range(len(value)):
        tring += f'\n{library[key][i]["title"]:45} '
        tring += f'{library[key][i]["author"]:40} '
        tring += f'{library[key][i]["year"]}'
    if I2 != 2:
        tring += f'\n{dash}{dash2}'
        I2 += 1
print(tring)
