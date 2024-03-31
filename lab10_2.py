try:
    with open("test.txt", "r") as file:
        data = file.read()

        if not data:
            raise Exception("Файл пустой")

        print("Информация из файла:")
        print(data)

except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print(e)
