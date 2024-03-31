def add_two_to_number():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = number + 2
        print(f"Результат сложения 2 и {number}: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

add_two_to_number()
add_two_to_number()
add_two_to_number()
