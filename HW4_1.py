print('Задание №4 - 1')
'''Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.'''

import random, timeit, cProfile

# постановка задачи
SIZE_M = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)]

# решение задачи HW3_7
# 1 способ
print('Решение задачи вариант №1')


def first_way(array: list):
    first_min = array[0]
    second_min = array[1]
    if first_min > second_min:
        first_min, second_min = second_min, first_min
    for i in range(2, len(array)):
        if array[i] < first_min:
            second_min = first_min  # чтобы не потерять преднаименьшее число
            first_min = array[i]
        elif array[i] < second_min:
            second_min = array[i]
    return f'первое минимальное число = {first_min}, второе минимальное число = {second_min}'


print(first_way(array))
print('*' * 100)

# 2 способ
print('Решение задачи вариант №2')


def second_way(array: list):
    first_min = min(array)
    new_array = array.copy()
    new_array.pop(new_array.index(first_min))
    second_min = min(new_array)
    return f'первое минимальное число = {first_min}, второе минимальное число = {second_min}'


print(second_way(array))
print('*' * 100)

# 3 способ

print('Решение задачи вариант №3')


def third_way(array: list):
    first_min = MAX_ITEM
    second_min = MAX_ITEM
    new_array = array.copy()
    for i in array:
        if i < first_min:
            first_min = i
    for i in range(len(array)):
        if array[i] == first_min:
            new_array.pop(i)
            break
    for i in new_array:
        if i == first_min:
            second_min = first_min
            break
        elif i < second_min:
            second_min = i
    return f'первое минимальное число = {first_min}, второе минимальное число = {second_min}'


print(third_way(array))
print('*' * 100)

print('Решение задачи вариант №4 для проверки')


def check_way(array: list):  # использем сортировку для проверки правильности решений и проанлизиреум скорость
    array.sort()
    return f'первое минимальное число = {array[0]}, второе минимальное число = {array[1]}'


print(check_way(array))

# print(timeit.timeit('first_way(array)', number=1000, globals=globals()))  # SIZE=10      0.001065499999999997
# print(timeit.timeit('first_way(array)', number=1000, globals=globals()))  # SIZE=100     0.007049799999999995
# print(timeit.timeit('first_way(array)', number=1000, globals=globals()))  # SIZE=1000    0.0736589
# print(timeit.timeit('first_way(array)', number=1000, globals=globals()))  # SIZE=10000   0.8005634
# print(timeit.timeit('first_way(array)', number=1000, globals=globals()))  # SIZE=100000  8.0252967

# print(timeit.timeit('second_way(array)', number=1000, globals=globals())) # SIZE=10      0.0009730000000000016
# print(timeit.timeit('second_way(array)', number=1000, globals=globals())) # SIZE=100     0.0035861999999999977
# print(timeit.timeit('second_way(array)', number=1000, globals=globals())) # SIZE=1000    0.031421599999999994
# print(timeit.timeit('second_way(array)', number=1000, globals=globals())) # SIZE=10000   0.3222722
# print(timeit.timeit('second_way(array)', number=1000, globals=globals())) # SIZE=100000  2.521200800000001

# print(timeit.timeit('third_way(array)', number=1000, globals=globals()))  # SIZE=10      0.00208609999390319
# print(timeit.timeit('third_way(array)', number=1000, globals=globals()))  # SIZE=100     0.0012348000018391758
# print(timeit.timeit('third_way(array)', number=1000, globals=globals()))  # SIZE=1000    0.06809129999601282
# print(timeit.timeit('third_way(array)', number=1000, globals=globals()))  # SIZE=10000   0.45030850000330247
# print(timeit.timeit('third_way(array)', number=1000, globals=globals()))  # SIZE=100000  4.359256800002186

# print(timeit.timeit('check_way(array)', number=1000, globals=globals()))  # SIZE=10      0.00030479999999999396
# print(timeit.timeit('check_way(array)', number=1000, globals=globals()))  # SIZE=100     0.0011092000000000046
# print(timeit.timeit('check_way(array)', number=1000, globals=globals()))  # SIZE=1000    0.005864399999999992
# print(timeit.timeit('check_way(array)', number=1000, globals=globals()))  # SIZE=10000   0.058392199999999894
# print(timeit.timeit('check_way(array)', number=1000, globals=globals()))  # SIZE=100000  0.4400687999999988


# cProfile.run('first_way(array)')

'''5 function calls in 0.549 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.549    0.549 <string>:1(<module>)
        1    0.549    0.549    0.549    0.549 HW4_1.py:17(first_way)
        1    0.000    0.000    0.549    0.549 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

# cProfile.run('second_way(array)')

'''9 function calls in 0.360 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.053    0.053    0.360    0.360 <string>:1(<module>)
        1    0.000    0.000    0.306    0.306 HW4_1.py:33(second_way)
        1    0.000    0.000    0.360    0.360 {built-in method builtins.exec}
        2    0.250    0.125    0.250    0.125 {built-in method builtins.min}
        1    0.049    0.049    0.049    0.049 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
        1    0.007    0.007    0.007    0.007 {method 'pop' of 'list' objects}

'''

# cProfile.run('third_way(array)')

'''6 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.006    0.006    0.006    0.006 HW4_1.py:55(way_1)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}'''

# cProfile.run('check_way(array)')

'''5 function calls in 0.092 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.092    0.092 <string>:1(<module>)
        1    0.000    0.000    0.092    0.092 HW4_1.py:43(third_way)
        1    0.000    0.000    0.092    0.092 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.092    0.092    0.092    0.092 {method 'sort' of 'list' objects}

'''

'''Выводы:
1. По результатам замеров с помощью timeit определена О(n). Выглядим справедливым тк по своей сути все способы 
перебирают полученный массив по каждому элементу и скорость выполнения меняется с увеличением объема массива.
2. С помощью cProfile были исследованы 3 способа нахождения 2 наименьших элементов массива. В результате исследования 
подтверждено что 1й способ использующий только циклы и условные операторы является самым медленным из трех,
циклы находящиеся внутри функции first_way выполняются довольно медленно. 
2 способ  значительно быстрее справляется с решением задачи, наибольшее время занимает функция min которая 
вызывается 2 раза. 
3 способ является небольшой модификацией первого способа и скорость зависит совпадает первое минимальное число со вторыи и на 
каком этапе цикла, что незначительно, но позволило увеличить скорость выполнения скрипта.
4. Для проверки решений использовался метод sort. Анализе показывает, что он наиболее удачное решение данной задачи, жаль, что 
использовать его нельзя..
'''
