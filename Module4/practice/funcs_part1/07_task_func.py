# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43
number = 29143
def n_f(number):
    hours = number // 3600
    a = number - hours * 3600
    minutes = a // 60
    b = a - minutes * 60
    seconds = b
    if len(str(hours)) < 2:
        hours = "0" + str(hours)
    if len(str(minutes)) < 2:
        minutes = "0" + str(minutes)
    if len(str(seconds)) < 2:
        seconds = "0" + str(seconds)
    return f"{hours}:{minutes}:{seconds}"
print(n_f(number))
