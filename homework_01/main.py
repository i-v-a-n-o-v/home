"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*n):
    sq = []
    for i in n:
        sq.append(i**2)
    return sq
print (power_numbers(1, 2, 5, 7))
"""
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def odd(in_num):
    if(in_num % 2) == 1:
        return True
    else:
        return False
def even(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False
def is_prime(in_num):
    k = 0
    for i in range(2, in_num // 2+1):
        if (in_num % i == 0):
            k = k+1
    if (k <= 0):
        return True
    else:
        return False

def filter_numbers(li, func):
    if func == ODD:
      out_filter = filter(odd, li)
    if func == EVEN:
      out_filter = filter(even, li)
    if func == PRIME:
      out_filter = filter(is_prime, li)
    print(list(out_filter))

filter_numbers([1, 2, 3], ODD)
filter_numbers([2, 1, 3, 5, 4], EVEN)
filter_numbers([1, 2, 3,300], PRIME)
