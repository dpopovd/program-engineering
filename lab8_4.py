from lab8_2 import Book

class Audiobook(Book):
    def __init__(self, title, author, genre, year_published, num_pages, duration):
        super().__init__(title, author, genre, year_published, num_pages)
        self.__duration = duration
        self.__played = False

    def get_book_info(self):
        base_info = super().get_book_info()
        return base_info + f", Продолжительность: {self.__duration} минут"

    def play(self):
        if not self.__played:
            self.__played = True
            print(f"Аудиокнига '{self.title}' начала воспроизведение.")
        else:
            print(f"Аудиокнига '{self.title}' уже была воспроизведена.")

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def has_been_played(self):
        return self.__played


my_audiobook = Audiobook("Основы Python. Научитесь думать как программист", "Аллен Б. Дауни", "Классика", 2021, 306, 360)

print("Информация об аудиокниге:")
print(my_audiobook.get_book_info())

print("\nВоспроизведение аудиокниги...")
my_audiobook.play()

print("\nПопытка повторного воспроизведения аудиокниги...")
my_audiobook.play()

print("\nТекущая продолжительность аудиокниги:", my_audiobook.get_duration(), "минут")
my_audiobook.set_duration(400)
print("Новая продолжительность аудиокниги:", my_audiobook.get_duration(), "минут")

print("\nБыла ли аудиокнига воспроизведена?", my_audiobook.has_been_played())
