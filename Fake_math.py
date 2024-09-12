# import random

def divide(first, second):
    if second == 0:
        return ('Ошибка! На ноль делить нельзя!')
    else:
        return first / second


#
# for i in range(10):
#     first = random.randint(1, 10)
#     second = random.randint(0, 10)
#     result = divide(first, second)
#     print("Fake_math = ", result)