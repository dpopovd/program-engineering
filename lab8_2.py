class Book:
    def __init__(self, title, author, genre, year_published, num_pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.year_published = year_published
        self.num_pages = num_pages
        self.is_checked_out = False
        self.user_rating = None

    def get_book_info(self):
        return f"{self.title}, автор {self.author}, Жанр: {self.genre}, Дата выхода: {self.year_published}"

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"Книга  '{self.title}' выдана")
        else:
            print(f"Книга  '{self.title}' уже выдана.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"Книга '{self.title}' возвращена.")
        else:
            print(f"Книга  '{self.title}' уже в библиотеке.")

    def rate_book(self, rating):
        if 1 <= rating <= 5:
            self.user_rating = rating
            print(f"Спасибо за оценку книги '{self.title}' {rating} звезды.")
        else:
            print("Неверная оценка. Пожалуйста, поставьте оценку от 1 до 5.")

# Создание объекта класса Book
my_book = Book("Основы Python. Научитесь думать как программист", "Аллен Б. Дауни", "Классика", 2021, 306)

print("\nОценка книги...")
my_book.rate_book(4.5)

print("\nПолучение оценки пользователей...")
print("Рейтинг пользователей:", my_book.user_rating)
