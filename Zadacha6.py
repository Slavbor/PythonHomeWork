# Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
# 385916 -> yes
# 123456 -> no
ticket = int(input("Enter ticket number(any length): "))
ticket_memory = ticket
count = 0
sum1 = 0
sum2 = 0
while ticket != 0:
    count += 1
    ticket //= 10
ticket = ticket_memory
if count % 2 == 0:
    for i in range(count // 2):
        last_digit = ticket % 10
        sum1 += last_digit
        ticket //= 10
    for j in range(count // 2):
        last_digit = ticket % 10
        sum2 += last_digit
        ticket //= 10
else:
    for i in range(count // 2):
        last_digit = ticket % 10
        sum1 += last_digit
        ticket //= 10
    ticket //= 10
    for j in range(count // 2):
        last_digit = ticket % 10
        sum2 += last_digit
        ticket //= 10
print("YES, lucky ticket") if sum1 == sum2 else print("Увы и ах")