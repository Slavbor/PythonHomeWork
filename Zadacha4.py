# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал
# каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
#
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
cranes = int(input("Enter cranes numbers: "))
if cranes == cranes // 3 * 2 + cranes // 3:
    print('Катя:', cranes // 3 * 2, "жур.", "Петя и Сережа по", int(cranes / 3 / 2), "жур.")
else:
    print("Не соответствует исходным параметрам")
