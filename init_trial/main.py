# from my_module.add import add, add_three
# from my_module.sub import sub
from my_module import add, sub, add_three
from nested_mod import mul, square, calculate

print(add(15, 20))
print(add_three(11, 10, 11))
print(sub(50, 20))
print(mul(5, 5))
print(square(5))
print(calculate(5, 4))
