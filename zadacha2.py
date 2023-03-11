# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


threeDigitNumber = int(input("Enter three digit number: "))

first_number = threeDigitNumber % 10
second_number = threeDigitNumber // 10 % 10
third_number = threeDigitNumber // 100 % 10
print(first_number + second_number + third_number)
