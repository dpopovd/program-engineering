def emp_test(log_tuple, emp_test_id):
    if emp_test_id not in log_tuple:
        return ()

    index1 = log_tuple.index(emp_test_id)

    if log_tuple.count(emp_test_id) == 1:
        return log_tuple[index1:]

    index2 = log_tuple.index(emp_test_id, index1 + 1)

    return log_tuple[index1:index2 + 1]

data = [
    ((1, 2, 3), 8),
    ((1, 8, 3, 4, 8, 8, 9, 2), 8),
    ((1, 2, 8, 5, 1, 2, 9), 8)
]

for log_tuple, emp_test_id in data:
    print(emp_test(log_tuple, emp_test_id))
