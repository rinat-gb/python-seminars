# 30. Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
#
# import math
#
# n = float(input('Введите число: '))
# while True:
#     d = float(input('Введите требуемую точность: '))
#     if d < 1.0:
#         break
#     print('Точность должна быть меньше единицы!')
#
# f = -(int(math.log10(d)))
#
# print(f'Число {n} с точностью {d} равно: {round(n, f)}' )
#

# 31. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
#
# n = int(input('Введите натуральное число: '))
# prime_num_lst = []

# for i in range(2, n+1):
#     for j in prime_num_lst:
#         if i % j == 0:
#             break
#     else:
#         prime_num_lst.append(i)

# multiplier_lst = []

# i = len(prime_num_lst) - 1
# tmp = n
# while i >= 0:
#     while not tmp % prime_num_lst[i]:
#         multiplier_lst.insert(0, prime_num_lst[i])
#         tmp //= prime_num_lst[i]
#     i -= 1

# multiplier_str = '*'.join(map(str, multiplier_lst))
# print(f'Простые множители для числа {n}: {multiplier_str}')

# 32. Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
#
# import numpy

# lst = input('Введите последовательность через запятую: ').split(',')
# unique_lst = numpy.unique(numpy.array(lst))
# print(unique_lst)
#