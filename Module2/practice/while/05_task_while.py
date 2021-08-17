# Вывод символов по диагоналям
# Даны сторона квадрата. Вывести его диагонали символами #.
# Формат входных данных: На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных: Требуется вывести диагонали символами # (см. примеры)
# Примеры:
# a = 6
#    #
 #  #
  ##
  ##
 #  #
#    #

# a = 3
# #
 #
# #


# TODO: your code here
n = int(input("Введите длинну квадрата: "))
list_a = []
n -= 1
i = 0
while i <= n:
    if i == 0 or i == n:
        list_a.append("X")
        i += 1
    else:
        list_a.append(" ")
        i += 1
final_text = "".join(list_a)

if n % 2 != 0:
    i = 0
    while list_a[i + 1] != "X" and list_a[n - 1] != "X":
        i += 1
        n -= 1
        list_a[i] = "X"
        list_a[i - 1] = " "
        list_a[n] = "X"
        list_a[n + 1] = " "
        final_text += "\n" + "".join(list_a)
    turn_text = "\n" + final_text[::-1]
    final_text += turn_text
else:
    i = 0
    while i != n:
        i += 1
        n -= 1
        list_a[i] = "X"
        list_a[i - 1] = " "
        list_a[n] = "X"
        list_a[n + 1] = " "
        final_text += "\n" + "".join(list_a)
    turn_text = final_text[::-1]
    row_exc = turn_text.find("\n") + 1
    turn_text = turn_text[row_exc:]
    final_text += "\n" + turn_text
print(final_text)
