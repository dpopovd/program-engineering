def main():
    sentences = ["London is the capital of the United Kingdom",
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
if __name__ == "__main__":
    main()