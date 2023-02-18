''' Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
Пример:   10 -> 1 2 4 8'''

N = int(input('Введите число N: '))
number = []
degree = 0
i = 0
while degree<N:
    degree = 2**i
    if degree>N:
        break
    number.append(degree)
    i += 1
print(number)

