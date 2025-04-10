from loguru import logger


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
            logger.error(f'Читатель {reader.name} не может '
                         f'зарезервировать книгу {self.book_name}')
        else:
            self.reserved = reader.name
            logger.debug(f'Читатель {reader.name} зарезервировал '
                         f'книгу {self.book_name}')

    def cancel_reserve(self, reader):
        if reader.name == self.reserved:
            logger.debug(f'Читатель {reader.name} снимает резервацию '
                         f'с книги {self.book_name}')
            self.reserved = None
        else:
            logger.error(f'Читатель {reader.name} не может снять с '
                         f'резервации книгу {self.book_name}')

    def get_book(self, reader):
        if ((self.reserved == reader.name or self.reserved is None)
                and self.received is None):
            logger.debug(f'Читатель {reader.name} забирает книгу '
                         f'{self.book_name} с собой')
            self.reserved = None
            self.received = reader.name
        else:
            logger.error(f'Читатель {reader.name} не может забрать '
                         f'книгу {self.book_name}')

    def return_book(self, reader):
        if self.received == reader.name:
            logger.info(f'Читатель {reader.name} возвращает '
                        f'книгу {self.book_name}')
            self.received = None
        else:
            logger.critical(f'Читатель {reader.name} не может вернуть '
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
