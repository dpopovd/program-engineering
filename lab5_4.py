rating1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
rating2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
rating3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def fix_rating(rating):
    for i in range(len(rating)):
        if rating[i] == 2:
            rating[i] = None
        elif rating[i] == 3:
            rating[i] = 4
    return [grade for grade in rating if grade is not None]

upd_rating1 = fix_rating(rating1)
upd_rating2 = fix_rating(rating2)
upd_rating3 = fix_rating(rating3)

print("Обновленный список оценок 1:", upd_rating1)
print("Обновленный список оценок 2:", upd_rating2)
print("Обновленный список оценок 3:", upd_rating3)