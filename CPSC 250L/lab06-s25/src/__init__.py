class Book:
    def __init__(self, title, author, genre, subgenre, publisher):
        self.title = title
        self.author = author
        self.genre = genre
        self.subgenre = subgenre
        self.publisher = publisher

    def __str__(self):
        # Return a string representation of the book, formatted with aligned columns.
        return f"{self.author:25} | {self.title:40} | {self.publisher:15}"

class Library:
    def __init__(self):
        self.books = {'fiction': [], 'nonfiction': [], 'textbook': []}

    def add_book(self, book):
        # Add book to appropriate genre category.
        if book.genre == 'fiction' or book.genre == 'nonfiction':
            self.books[book.genre].append(book)
        else:
            self.books['textbook'].append(book)

    def __str__(self):
        result = ""
        for genre, books in self.books.items():
            result += f"\n{genre.capitalize()} Books:\n"
            books.sort(key=lambda b: (b.author, b.title, b.publisher))  # Sort books by author, title, then publisher
            for book in books:
                result += f"{book}\n"
        return result

def main(file_name):
    # Initialize library
    library = Library()

    # Read from the file
    with open(file_name, 'r') as file:
        for line in file:
            # Skip lines starting with #
            if line.startswith('#'):
                continue
            # Split the line by TAB and create a Book object
            fields = line.strip().split('\t')
            if len(fields) == 6:
                title, author, genre, subgenre, height, publisher = fields
                # Ignore height, we don't need it.
                book = Book(title, author, genre, subgenre, publisher)
                # Add book to library
                library.add_book(book)

    # Print the library
    print(library)

if __name__ == "__main__":
    main('data/big_list.txt')
