list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def transform(lst):
    result_set = set()
    for num in lst:
        if lst.count(num) > 1:
            temp = str(num) * lst.count(num)
            result_set.add(temp)
        else:
            result_set.add(num)
    return result_set

result_1 = transform(list_1)
result_2 = transform(list_2)
result_3 = transform(list_3)

print(result_1)
print(result_2)
print(result_3)