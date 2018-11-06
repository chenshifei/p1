from math import pi
from random import random

def circle_area(radius):
    return pi * radius ** 2

def triangle_area(base, height):
    return base * height / 2

def tripler(s):
    return str(s) * 3

def fruitval(fruit):
    if fruit == 'banana':
        return 10
    elif fruit == 'apple':
        return 7
    else:
        return 3

def one_of(n, v1, v2):
    if n <= 0 or not isinstance(n, int):
        print('n should be a natural number')
        return

    if n % 2 == 0:
        return v2
    else:
        return v1

def five():
    for n in range(1000, 1050, 10):
        print(n)

def odd_part(n):
    while n % 2 == 0:
        n = n / 2
    return n

def countrand(limit):
    sum = 0
    step = 0
    while sum < limit:
        v = random()
        print('Step', step, ': add by', v)
        sum += v
        step += 1
    return step

