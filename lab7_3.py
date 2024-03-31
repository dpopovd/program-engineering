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
