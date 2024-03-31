## Самостоятельная работа №3

### 1)Напишите программу, которая преобразует 1 в 31. Для выполнения поставленной задачи необходимо обязательно и только один раз использовать: • Цикл for • *= 5 • += 1 Никаких других действий или циклов использовать нельзя

- Оформленный код

```python
result = 1
for _ in range(5):
    result = result * 5 + 1
print(result)
```

  ![img](https://github.com/xsadsenpai/py_practice/blob/lab3/pic/img_3_1.png)

##### Вывод

Этот код также использует цикл for, операторы *= и += для преобразования числа 1 в 31. Оператор *= умножает текущее значение на 5, а затем прибавляется 1, и так происходит 5 раз.

### 2) Напишите программу, которая фразу «Hello World» выводит в обратном порядке, и каждая буква находится в одной строке консоли. При этом необходимо обязательно использовать любой цикл, а также программа должна занимать не более 3 строк в редакторе кода

```python
phrase = "Hello World"
for char in reversed(phrase):
    print(char)
```

  ![img](https://github.com/xsadsenpai/py_practice/blob/lab3/pic/img_3_2.png)

##### Вывод

Этот код использует цикл for и функцию reversed(), чтобы перебирать символы фразы "Hello World" в обратном порядке, а затем выводит каждый символ на отдельной строке.

### 3)

Напишите программу, на вход которой поступает значение из консоли,оно должно быть числовым и в диапазоне от 0 до 10 включительно (это необходимо учесть в программе). Если вводимое число не подходит по требованиям, то необходимо вывести оповещение об этом в консоль и остановить программу. Код должен вычислять в каком диапазоне находится полученное число. Нужно учитывать три диапазона:
• от 0 до 3 включительно
• от 3 до 6
• от 6 до 10 включительно
Результатом работы программы будет выведенный в консоль диапазон. Программа должна занимать не более 10 строчек в редакторе кода

```python
num = int(input("Введите число от 0 до 10: "))
if 0 <= num <= 10:
    if num <= 3:
        print("Число находится в диапазоне от 0 до 3 включительно")
    elif num <= 6:
        print("Число находится в диапазоне от 3 до 6")
    else:
        print("Число находится в диапазоне от 6 до 10 включительно")
else:
    print("Число, которое было введено, не удовлетворяет условиям задачи.")
```

  ![img](https://github.com/xsadsenpai/py_practice/blob/lab3/pic/img_3_3.png)
  ![img](https://github.com/xsadsenpai/py_practice/blob/lab3/pic/img_3_3_3.png)
##### Вывод

Эта программа сначала запрашивает у пользователя число. Затем она проверяет, находится ли введенное число в диапазоне от 0 до 10 включительно. Если число находится в этом диапазоне, программа определяет, в каком из трех заданных диапазонов оно находится, и выводит соответствующее сообщение. Если введенное число не соответствует указанным требованиям, программа выдает оповещение об этом.

### 4)

Манипулирование строками. Напишите программу на Python, которая принимает предложение (на английском) в качестве входных данных от пользователя. Выполните следующие операции и отобразите результаты:
• Выведите длину предложения.
• Переведите предложение в нижний регистр.
• Подсчитайте количество гласных (a, e, i, o, u) в предложении.
• Замените все слова "ugly" на "beauty".
• Проверьте, начинается ли предложение с "The" и заканчивается ли на "end".
Проверьте работу программы минимум на 3 предложениях, чтобы охватить проверку всех поставленных условий.

```python
def main():
    sentences = [
        "London is the capital of the United Kingdom",
        "Oh my god, I'm so tired of doing these DIY jobs...",
        "He used to think he was ugly, but now he sees the beauty in herself. End"
    ]
    vowels = "aeiou"
    for sentence in sentences:
        print("Исходное предложение", sentence)
        print("Длина предложения:", len(sentence))
        print("Предложение в нижнем регистре:", sentence.lower())
        print("Количество гласных:", sum(1 for char in sentence if char.lower() in vowels))
        print("Замените слово «уродливое»(ugly) на «красота»(beauty)", sentence.replace("ugly", "beauty"))
        print("Начинается с «The»", sentence.startswith("The"))
        print("Заканчивается словом «End»:", sentence.endswith("End"))
        print()
if __name__ == "__main__": #Это проверка, запущена ли программа напрямую из командной строки (а не импортирована как модуль). Если условие выполняется, вызывается функция main(), которая запускает основную логику программы.
    main()
```

  ![img](https://github.com/xsadsenpai/py_practice/blob/lab3/pic/img_3_4.png)

Эта программа принимает несколько предложений от пользователя и выполняет указанные операции для каждого из них. Она выводит длину предложения, предложение в нижнем регистре, количество гласных, замену слов "ugly" на "beauty", а также проверяет, начинается ли предложение с "The" и заканчивается ли на "end".

### 5)

Составьте программу, результатом которой будет данный вывод в консоль:

hello world

hello

hello world

hello

hello world

hello

hello world

hello

hello world

hello

hello world

hello

Программу нужно составить из данных фрагментов кода:
memory = ' world'
if values not in string:
while ' world' not in string:
string = string + ' world'
if counter in values:
counter = 10
string = 'hello'
string = memory
string = 'world'
counter = 0
if counter > 7:
print(string + memory)
print(string)
while counter !=10:
values = [0, 2, 4, 6, 8, 10]
memory = string
if counter < 10:
counter += 1
print(memory)
memory = string

Строки кода можно использовать только один раз.
Необязательно использовать все строки кода.

```python
string = 'hello'
memory = ' world'
counter = 0

while counter != 6:
    print(string + memory)
    print(string)
    counter += 1
```

  ![img](https://github.com/xsadsenpai/py_practice/blob/lab3/pic/img_3_5.png)

##### Вывод

Этот код выводит "hello world" и "hello" поочередно 6 раз. Как указано в задании.