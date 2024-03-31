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
