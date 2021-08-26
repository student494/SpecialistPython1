# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

x1 = 7
y1 = 6
R1 = 1
x2 = 9
y2 = 8
R2 = 4
line_between_centers = distance(x1, y1, x2, y2)
if R1 > R2 and R2 + line_between_centers <= R1:
    print("Одна окружность внутри другой")
elif R1 <= R2 and R1 + line_between_centers <= R2:
    print("Одна окружность внутри другой")
else:
    print("Окружности не совмещены")
