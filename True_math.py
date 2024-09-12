# import random
from math import inf

def divide_2(first, second):
    if second == 0:
        return inf
    else:
        return first / second
#
#
# for i in range(10):
#     first = random.randint(1, 10)
#     second = random.randint(0, 10)
#     result = divide_2(first, second)
#     print("True_math = ", result)