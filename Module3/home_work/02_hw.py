# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here
qtt_el = int(input("Введите количество элементов в списке: "))
i = 1
while i <= qtt_el:
    rnd_int = random.randint(-100, 100)
    numbers.append(rnd_int)
    i += 1
print(numbers)
