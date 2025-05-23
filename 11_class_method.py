# 11. class method

class Book:
    total_books = 0 

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count() 

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books


# Example usage:
book1 = Book("Python Crash Course", "Eric Metthes")
book2 = Book("Clean Code", "Robert C.Martin")

print("Total books:", Book.get_total_books()) 
