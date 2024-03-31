def calc_treug(a, b, c):
    # Вычисление полупериметра
    s = (a + b + c) / 2
    # Вычисление площади по формуле Герона
    treug = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return treug