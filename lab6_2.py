def rem(tup, value):
    try:
        index = tup.index(value)
        return tup[:index] + tup[index + 1:]
    except ValueError:
        return tup

data = [
    ((1, 2, 3), 1),
    ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
    ((2, 4, 6, 6, 4, 2), 9)
]

for tup, value in data:
    print(rem(tup, value))
