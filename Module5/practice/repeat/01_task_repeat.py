# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random
def gen_list(n, r1, r2):
    list_a = []
    while len(list_a) < n:
        rnd_int = random.randint(r1, r2)
        list_a.append(rnd_int)
    return list_a

list_1 = gen_list(5, -100, 100)

print(list_1)
