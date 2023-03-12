# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой
# между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

choko_size1 = int(input("Введите первое количество долек шоколадки: "))
choko_size2 = int(input("Введите второе количество долек шоколадки: "))
breakOff = int(input("Введите сколько долек хотите отломить: "))
max = choko_size1
if choko_size2 > choko_size1:
    max = choko_size2
for i in range(1, max + 1):
    if i * choko_size1 == breakOff:
        print("YES")
        break
    elif i * choko_size2 == breakOff:
        print("YES")
        break
else:
    print("NO")
