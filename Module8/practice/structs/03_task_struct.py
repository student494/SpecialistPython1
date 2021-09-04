# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
from random import randint
list_a =[]
i = randint(1, 100)
for _ in range(i):
    list_a.append(randint(1, 100))
list_not_high_10 = []
sum_pos_el = 0
for el in list_a:
    if el <= 10:
        list_not_high_10.append(el)
for el in list_a:
    if el > 0:
        sum_pos_el += el
aver_num = sum(list_a)/len(list_a)
print(list_not_high_10)
print(sum_pos_el)
print(aver_num)
