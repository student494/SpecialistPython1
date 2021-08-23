# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    list_numbers = []
    while ticket_number > 0:
        list_numbers.append(ticket_number % 10)
        ticket_number //= 10
    if sum(list_numbers[:3]) == sum(list_numbers[3:]):
        return "билет счастливый"
    else:
        return "билет обычный"


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(123321))
print(lucky_ticket(436751))
