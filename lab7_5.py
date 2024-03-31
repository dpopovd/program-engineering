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
