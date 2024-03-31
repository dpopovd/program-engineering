# Файл lab8_5.py
from lab8_2 import Book

class Audiobook(Book):
    def __init__(self, title, author, genre, year_published, num_pages, duration):
        super().__init__(title, author, genre, year_published, num_pages)
        self.__duration = duration
        self.__played = False

    def get_book_info(self):
        return f"Аудиокнига: {self.title} (автор: {self.author}), Продолжительность: {self.__duration} минут"

    def play(self):
        if not self.__played:
            self.__played = True
            print(f"Началось воспроизведение аудиокниги '{self.title}'.")
        else:
            print(f"Аудиокнига '{self.title}' уже была воспроизведена.")

# Создаем экземпляр аудиокниги
audiobook = Audiobook("Война и мир", "Лев Толстой", "Роман", 1869, 1225, 1800)

# Выводим информацию об аудиокниге
print(audiobook.get_book_info())
