"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    power_lst = [i**2 for i in num]
    return power_lst

def is_prime(lst):
    res = []
    for i in lst:
        if i == 2:
            res.append(i)
        elif i%2:
            for j in range(3, i+1):
                if i == j:
                    res.append(i)
                    break
                elif i%j == False:
                    break
    return res
# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(lst_nums, fil):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    res = []
    if fil == ODD:
        res = list(filter(lambda x: x%2, lst_nums))
    elif fil == EVEN:
        res = list(filter(lambda x: x%2 == False, lst_nums))
    else:
        res = is_prime(lst_nums)
    return res