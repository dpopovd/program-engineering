class Book:
    def __init__(self, title, author, genre, year_published):
        self.title = title
        self.author = author
        self.genre = genre
        self.year_published = year_published
        self.is_checked_out = False

    def get_book_info(self):
        return f"{self.title}, автор {self.author}, Жанр: {self.genre}, Дата выхода: {self.year_published}"

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"Книга '{self.title}' была проверена.")
        else:
            print(f"Книга '{self.title}' уже проверена.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"Книга '{self.title}' возвращена.")
        else:
            print(f"The book '{self.title}' уже есть в библиотеке.")
my_book = Book("Основы Python. Научитесь думать как программист", "Аллен Б. Дауни", "Классика", 2021)

print("О книге:")
print("Название:", my_book.title)
print("Автор:", my_book.author)
print("Жанр:", my_book.genre)
print("Дата выхода:", my_book.year_published)

print("\nО книге:", my_book.get_book_info())

print("\nПроверяю книгу...")
my_book.check_out()

print("\nВозвращение книги...")
my_book.return_book()

print("\nПытаюсь перечитать книгу еще раз...")
my_book.check_out()
