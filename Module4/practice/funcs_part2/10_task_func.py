# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов


def average(*args):
i = len(args)
find_sum = 0
for el in args:
    find_sum += el
find_sum /= i
return find_sum


print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
