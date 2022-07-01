# from classes_and_objects_exercises.library.project.user import User
from .user import User


class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        for book in self.rented_books.values():
            if book_name in book.keys():
                return f'The book "{book_name}" is already rented and will be available in {self.rented_books[user.username][book_name]} days!'
        user.books.append(book_name)
        self.rented_books[user.username] = {}
        self.rented_books[user.username][book_name] = days_to_return
        self.books_available[author].remove(book_name)
        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]
        user.books.remove(book_name)



