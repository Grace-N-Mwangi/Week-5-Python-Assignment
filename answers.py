class Book:
    """
    Represents a physical book.
    """
    def __init__(self, title, author, pages):
        """
        Initializes the Book object with title, author, and number of pages.
        """
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        """
        Simulates reading the book.
        """
        return f"You're reading '{self.title}' by {self.author}, which has {self.pages} pages."

    def info(self):
        """
        Returns basic information about the book.
        """
        return f"Book: '{self.title}', Author: {self.author}, Pages: {self.pages}"


class EBook(Book):
    """
    Represents an electronic version of a book.
    """
    def __init__(self, title, author, pages, file_size):
        """
        Initializes the EBook object with additional file size attribute.
        """
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def read(self):
        """
        Overrides the read method for EBook.
        """
        return f"You're reading '{self.title}' by {self.author} on your e-reader."

    def download(self):
        """
        Simulates downloading the eBook.
        """
        return f"Downloading '{self.title}'... File size: {self.file_size}MB"


# Using the classes
physical_book = Book("1984", "George Orwell", 328)
ebook = EBook("The Great Gatsby", "F. Scott Fitzgerald", 180, 1.5)

print(physical_book.info())
print(physical_book.read())
print(ebook.info())
print(ebook.read())
print(ebook.download())
