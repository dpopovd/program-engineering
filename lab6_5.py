def count_vowels(st):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = {vowel: 0 for vowel in vowels}

    for char in st.lower():
        if char in vowels:
            vowel_count[char] += 1

    return [vowel_count[vowel] for vowel in vowels]

data = [
    "Tuples (tuple type) are an immutable data type in Python that are used to store an ordered sequence of elements.",
    "These collections have three great properties:", # https://skillbox.ru/media/code/chto-takoe-kortezhi-v-python-i-kak-ikh-ispolzovat/
    "Immutability. Once a tuple is created, elements cannot be added to it, nor can they be modified or deleted. When you try to do this, the interpreter will throw a TypeError",
    "Orderliness. The elements of a tuple are arranged in a certain order, which is also immutable. Any element can be accessed by its index (ordinal number).",
    "The elements of a tuple can be objects of different data types: numbers, strings, lists, other tuples, and others. Collection elements can have unlimited nesting depth. For example, a tuple may contain a list, which will contain another list, which will again contain a list, and so on."
]

for st in data:
    print("Строка:", st)
    print("Количество гласных:", count_vowels(st))
    print()
