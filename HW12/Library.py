class Book:

    def __init__(self, book_name, author, num_pages,
                 isbn, reserved=None, received=None):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved = reserved
        self.received = received

    def reserve(self, reader):
        if self.reserved is not None:
            print(f'Читатель {reader.name} не может '
                  f'зарезервировать книгу {self.book_name}')
        else:
            self.reserved = reader.name
            print(f'Читатель {reader.name} зарезервировал '
                  f'книгу {self.book_name}')

    def cancel_reserve(self, reader):
        if reader.name == self.reserved:
            print(f'Читатель {reader.name} снимает резервацию '
                  f'с книги {self.book_name}')
            self.reserved = None
        else:
            print(f'Читатель {reader.name} не может снять с '
                  f'резервации книгу {self.book_name}')

    def get_book(self, reader):
        if ((self.reserved == reader.name or self.reserved is None)
                and self.received is None):
            print(f'Читатель {reader.name} забирает книгу '
                  f'{self.book_name} с собой')
            self.reserved = None
            self.received = reader.name
        else:
            print(f'Читатель {reader.name} не может забрать '
                  f'книгу {self.book_name}')

    def return_book(self, reader):
        if self.received == reader.name:
            print(f'Читатель {reader.name} возвращает '
                  f'книгу {self.book_name}')
            self.received = None
        else:
            print(f'Читатель {reader.name} не может вернуть '
                  f'книгу {self.book_name}')


class Reader:

    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        book.reserve(self)

    def cancel_reserve(self, book):
        book.cancel_reserve(self)

    def get_book(self, book):
        book.get_book(self)

    def return_book(self, book):
        book.return_book(self)


book = Book(book_name="The Hobbit", author="Books by J.R.R. Tolkien",
            num_pages=400, isbn="0006754023")

vasya = Reader("Vasya")
petya = Reader("Petya")

vasya.reserve_book(book)
petya.reserve_book(book)  # User can not reserve a book

vasya.cancel_reserve(book)
petya.reserve_book(book)

vasya.get_book(book)  # User can not get a book
petya.get_book(book)

vasya.return_book(book)  # User can not return a book
petya.return_book(book)

vasya.get_book(book)
