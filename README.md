## Самостоятельная работа №8

### 1)

Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

  ![img_8_1.png](https://github.com/xsadsenpai/py_practice/blob/lab8/pic/img_8_1.png)

##### Вывод
Этот код создает класс Book (Книга) в Python, который моделирует основные характеристики книги, такие как заголовок, автор, жанр и год публикации. Класс Book имеет методы для проверки книги и её возврата.

### 2)

Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

  ![img_8_2.png](https://github.com/xsadsenpai/py_practice/blob/lab8/pic/img_8_2.png)

##### Вывод

Этот код определяет класс Book, представляющий книгу, с методами для получения информации о книге, выдачи, возврата и оценки пользователем. Создается объект my_book, для которого вызывается метод rate_book для оценки книги и вывода пользовательской оценки.

### 3)

Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли```python

```python
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
```

  ![img_8_3.png](https://github.com/xsadsenpai/py_practice/blob/lab8/pic/img_8_3.png)

##### Вывод

Этот код создает класс Audiobook, который является дочерним классом класса Книга. Дочерний класс добавляет новый атрибут продолжительность и метод воспроизвести, который позволяет воспроизводить аудиокнигу.

### 4)

Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли

```python
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
```

  ![img_8_4.png](https://github.com/xsadsenpai/py_practice/blob/lab8/pic/img_8_4.png)

##### Вывод

Этот код создаёт класс Audiobook, который наследуется от класса Book. В классе Audiobook инкапсулированы атрибуты duration (продолжительность аудиокниги) и played (флаг, указывающий, была ли аудиокнига воспроизведена). Класс предоставляет методы для получения информации об аудиокниге, воспроизведения аудиокниги, а также для получения и изменения продолжительности и состояния воспроизведения. В конце кода создаётся экземпляр класса Audiobook, выводится информация об аудиокниге, проигрывается аудиокнига, делается попытка воспроизведения её снова, а затем тестируются методы для получения и изменения атрибутов.

### 5)

Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли

```python
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
```

  ![img_8_5.png](https://github.com/xsadsenpai/py_practice/blob/lab8/pic/img_8_5.png)

##### Вывод

Этот код создаёт класс Audiobook, который наследует атрибуты и методы класса Book. Класс Audiobook содержит информацию о аудиокниге, такую как название, автор и продолжительность, а также методы для получения информации об аудиокниге и воспроизведения его. В коде также создается экземпляр класса Audiobook с указанием его параметров и выводится информация о нем.






