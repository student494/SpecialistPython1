# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


xa = 1
ya = 1
xb = 3
yb = 5
xc = 10
yc = 4
AB = distance(xa, ya, xb, yb)
AC = distance(xa, ya, xc, yc)
BC = distance(xb, yb, xc, yc)
dict_line = dict(AB="отрезок AB", AC="отрезок AC", BC="отрезок BC")
min_line = min(dict_line)
print(f"Самый короткий {dict_line[min_line]}")  # Выводим название отрезка, например “АС”.
