from my_module import add, sub
from nested_mod import mul


def calculate(x, y):
    return mul(add(x, y), sub(x, y))
