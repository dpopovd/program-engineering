from lab8_2 import Book


class Audiobook(Book):
    def __init__(self, title, author, genre, year_published, num_pages, duration):
        super().__init__(title, author, genre, year_published, num_pages)
        self.duration = duration
        self.played = False

    def get_book_info(self):
        base_info = super().get_book_info()
        return base_info + f", Продолжительность: {self.duration} минут"

    def play(self):
        if not self.played:
            self.played = True
            print(f"Аудиокнига  '{self.title}' начала воспроизведение.")
        else:
            print(f"Аудиокнига  '{self.title}' уже была воспроизведена.")

my_audiobook = Audiobook("Основы Python. Научитесь думать как программист", "Аллен Б. Дауни", "Классика", 2021, 306, 360)

print("Информация об аудиокниге:")
print(my_audiobook.get_book_info())

print("\nВоспроизведение аудиокниги...")
my_audiobook.play()

print("\nПопытка повторного воспроизведения аудиокниги...")
my_audiobook.play()
