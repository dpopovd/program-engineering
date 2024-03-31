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
