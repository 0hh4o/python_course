from functools import partial

def curry_partial(func, *args, **kwargs):
    return partial(func, *args, **kwargs)

a = 5
def double():
    return a * 2

result = a * 2
assert curry_partial(curry_partial(double, a))() == result