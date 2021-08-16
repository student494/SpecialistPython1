# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
qtt_el = int(input("Введите количество элементов в списке: "))
numbers = []
i = 1
while i <= qtt_el:
    rnd_int = random.randint(-100, 100)
    numbers.append(rnd_int)
    i += 1
sum_elements = 0
for element in numbers:
    if element > 0 and element % 2 == 0:
        sum_elements += element
print(sum_elements)
