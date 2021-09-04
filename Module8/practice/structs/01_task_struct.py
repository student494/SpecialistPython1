# Бегун проводил ежедневные тренировки и записывал расстояния которые пробегал за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)
def dist_in_foot(*args):
    new_list = []
    for el in args:
        f = float(el) * 0.3048
        new_list.append(f)
    return new_list
print(dist_in_foot(*distances))
