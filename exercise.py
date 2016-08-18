from operator import mul
from functools import reduce

def multiply(*args):
    return reduce(mul, args)
def print_three(a, b, c):
    print(a, b, c)
def print_table(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
