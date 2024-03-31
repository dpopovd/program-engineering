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
