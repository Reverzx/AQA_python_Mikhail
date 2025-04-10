from HW21.source.Library import Book, Reader


class TestLibrary:
    def setup_method(self):
        self.book = Book(book_name="The Hobbit", author="Books by J.R.R. Tolkien",
                         num_pages=400, isbn="0006754023")
        self.vasya = Reader("Vasya")
        self.petya = Reader("Petya")

    def test_reserve_book(self):
        self.vasya.reserve_book(self.book)
        assert self.book.reserved == "Vasya"

    def test_reserve_book_blocked(self):
        self.vasya.reserve_book(self.book)
        self.petya.reserve_book(self.book)
        assert not self.book.reserved == "Petya"

    def test_cancel_reserve(self):
        self.vasya.reserve_book(self.book)
        self.vasya.cancel_reserve(self.book)
        assert self.book.reserved is None

    def test_cancel_reserve_by_wrong_reader(self):
        self.vasya.reserve_book(self.book)
        self.petya.cancel_reserve(self.book)
        assert self.book.reserved == "Vasya"

    def test_get_book(self):
        self.vasya.reserve_book(self.book)
        self.vasya.get_book(self.book)
        assert self.book.received == "Vasya"

    def test_get_book_without_reserve(self):
        self.vasya.get_book(self.book)
        assert self.book.received == "Vasya"

    def test_get_book_with_wrong_user(self):
        self.petya.reserve_book(self.book)
        self.vasya.get_book(self.book)
        assert not self.book.received == "Vasya"

    def test_return_book(self):
        self.vasya.reserve_book(self.book)
        self.vasya.get_book(self.book)
        self.vasya.return_book(self.book)
        assert self.book.received is None

    def test_return_book_with_wrong_user(self):
        self.vasya.reserve_book(self.book)
        self.vasya.get_book(self.book)
        self.petya.return_book(self.book)
        assert self.book.received is not None
