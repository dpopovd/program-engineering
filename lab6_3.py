def count_dig(s):
    dig_count = {}
    for dig in s:
        dig_count[int(dig)] = dig_count.get(int(dig), 0) + 1

    sorted_dig = sorted(dig_count.items(), key=lambda x: x[1], reverse=True)

    top_3_dig = {}
    for dig, count in sorted_dig[:3]:
        top_3_dig[dig] = count

    return top_3_dig

s = "7890574467890951"

result = count_dig(s)
print("Словарь из трех самых часто встречаемых чисел:", result)