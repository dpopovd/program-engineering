def average(*args):
    return sum(args) / len(args) if args else 0

if __name__ == "__main__":
    values = []  # Создаем список для хранения аргументов

    # Запрашиваем у пользователя числа, пока он не введет пустую строку
    while True:
        user_input = input("Введите число (или нажмите Enter для завершения ввода): ")
        if user_input == "":
            break
        try:
            values.append(float(user_input))  # Добавляем число в список
        except ValueError:
            print("Ошибка: Введите числовое значение или нажмите Enter для завершения ввода.")

    # Вызываем функцию average с аргументами из списка и выводим результат
    print("Среднее арифметическое:", average(*values))