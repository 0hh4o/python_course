def zero(func=None):
    if func:
        return func(0)
    return 0

def one(func=None):
    if func:
        return func(1)
    return 1

def two(func=None):
    if func:
        return func(2)
    return 2

def three(func=None):
    if func:
        return func(3)
    return 3

def four(func=None):
    if func:
        return func(4)
    return 4

def five(func=None):
    if func:
        return func(5)
    return 5

def six(func=None):
    if func:
        return func(6)
    return 6

def seven(func=None):
    if func:
        return func(7)
    return 7

def eight(func=None):
    if func:
        return func(8)
    return 8

def nine(func=None):
    if func:
        return func(9)
    return 9

def plus(num):
    return lambda x: x + num

def minus(num):
    return lambda x: x - num

def times(num):
    return lambda x: x * num

def divided_by(num):
    return lambda x: x // num

print(seven(times(five())))  # 输出: 35
print(four(plus(nine())))  # 输出: 13
print(eight(minus(three())))  # 输出: 5
print(six(divided_by(two())))  # 输出: 3
