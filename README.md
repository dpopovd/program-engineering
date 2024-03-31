## Самостоятельная работа №7

### Задание №1
- Текст задания

Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

- Оформленный код

```python
def count_words(file_name):
    try:
        word_count = {}
        max_count_word = ""
        max_count = 0

        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip(",.!?")
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1
                        if word_count[word] > max_count:
                            max_count = word_count[word]
                            max_count_word = word

        total_words = sum(word_count.values())
        unique_words = len(word_count)

        return total_words, unique_words, max_count_word, max_count
    except FileNotFoundError:
        print("Файл не найден.")
        return None
    except Exception as e:
        print("Произошла ошибка:", e)
        return None

file_name = "kontur.txt"

try:
    result = count_words(file_name)
    if result is not None:
        total_words, unique_words, most_common_word, max_count = result
        print("Самое часто встречающееся слово:", most_common_word)
        print("Количество его вхождений:", max_count)
except Exception as e:
    print("Произошла ошибка:", e)
```

- Скрины консоли

  ![img_7_1_1.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_1_1.png)

  ![img_7_1_2.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_1_2.png)

  ![img_7_1_3.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_1_3.png)

- Развернутый вывод

Код подтягивает файл с директории, посчитывает часто встречающие слова и сколько раз оно было использовано.

### Задание №2
- Текст задания

У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

- Оформленный код

```python
def save_expenses(expenses, filename):
    with open(filename, 'w') as file:
        for category, amount in expenses.items():
            file.write(f"{category}: {amount}\n")

def load_expenses(filename):
    expenses = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                category, amount = line.strip().split(': ')
                expenses[category] = float(amount)
    except FileNotFoundError:
        print("Файл с данными не найден. Создан новый файл.")
    return expenses

def print_expenses(expenses):
    if not expenses:
        print("Нет информации о расходах.")
    else:
        print("Расходы:")
        for category, amount in expenses.items():
            print(f"{category}: {amount}")


def main():
    expenses_file = "rashod.txt"
    expenses = load_expenses(expenses_file)

    while True:
        print("\nМеню:")
        print("1. Ввести новый расход")
        print("2. Показать текущие расходы")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            category = input("Введите категорию расхода: ")
            amount = float(input("Введите сумму расхода: "))
            expenses[category] = amount
            save_expenses(expenses, expenses_file)
            print("Расход успешно добавлен.")
        elif choice == '2':
            print_expenses(expenses)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие снова.")
if __name__ == "__main__":
    main()
```

- Скрины консоли

  ![img_7_2_1.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_2_1.png)

  ![img_7_2_2.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_2_2.png)

  ![img_7_2_3.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_2_3.png)

   ![img_7_2_4.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_2_4.png)

- Развернутый вывод

Через консоль есть возможность добавить категорию и указать текущие расходы. В сам файл вписываются данные.

### Задание №3
- Текст задания

Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

• Текст в файле:

Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

• Ожидаемый результат:

Input file contains:

108 letters

20 words

4 lines

- Оформленный код

```python
def analyze_text(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            num_letters = sum(c.isalpha() for c in text)
            num_words = len(text.split())
            num_lines = text.count('\n') + 1
            return num_letters, num_words, num_lines
    except FileNotFoundError:
        print("Файл не найден.")
        return None, None, None

file_name = "input.txt"

num_letters, num_words, num_lines = analyze_text(file_name)

if num_letters is not None and num_words is not None and num_lines is not None:
    print("Input file contains:")
    print(f"{num_letters} letters")
    print(f"{num_words} words")
    print(f"{num_lines} lines")
```

- Скрины консоли

  ![img_7_3_1.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_3_1.png)

  ![img_7_3_2.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_3_2.png)



- Развернутый вывод

Код загружает файл, анализирует и выводит статистику по тексту.

### Задание №4
- Текст задания

Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.

• Запрещенные слова:

hello email python the exam wor is

• Предложение для проверки:

Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!

• Ожидаемый результат:

*****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!

- Оформленный код

```python
def censor_sentence(sentence, forbidden_words):
    censored_sentence = sentence.lower()
    for word in forbidden_words:
        censored_sentence = censored_sentence.replace(word, '*' * len(word))
    return censored_sentence

def load_forbidden_words(file_name):
    try:
        with open(file_name, 'r') as file:
            forbidden_words = file.read().split()
            return forbidden_words
    except FileNotFoundError:
        print("Файл с запрещенными словами не найден.")
        return []

def main():
    forbidden_words_file = "input2.txt"
    sentence = input("Введите предложение для проверки: ")

    forbidden_words = load_forbidden_words(forbidden_words_file)

    censored_sentence = censor_sentence(sentence, forbidden_words)
    print("Предложение с замененными запрещенными словами:")
    print(censored_sentence)

if __name__ == "__main__":
    main()
```

- Скрины консоли

  ![img_7_4_1.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_4_1.png)

  ![img_7_4_2.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_4_2.png)



- Развернутый вывод

Код берет из файла слова, который в бане и заменяет на *** их в консоле, если они попадают в запрос.

### Задание №5
- Текст задания

Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

- Оформленный код

```python
def replace_word_in_file(file_name, old_word, new_word):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        with open(file_name, 'w') as file:
            for line in lines:
                new_line = line.replace(old_word, new_word)
                file.write(new_line)
    except FileNotFoundError:
        print("Файл не найден.")

def main():
    file_name = "input3.txt"
    old_word = input("Введите слово, которое нужно заменить: ")
    new_word = input("Введите новое слово: ")

    replace_word_in_file(file_name, old_word, new_word)
    print(f"Слово '{old_word}' успешно заменено на '{new_word}' в файле '{file_name}'.")

if __name__ == "__main__":
    main()
```

- Скрины консоли

  ![img_7_5_1.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_5_1.png)

  ![img_7_5_2.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_5_2.png)

  ![img_7_5_3.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_5_3.png)


- Развернутый вывод

Код спрашивает какое слово заменить в файле, находит его и заменяет на слово введенное в запросе.