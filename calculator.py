import math


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def division(a, b):
    if b == 0:
        raise ValueError("div by 0")
    return a / b


def multiplication(a, b):
    return a * b


def power(a, b):
    if b < 0:
        raise ValueError("incorrect")
    return math.pow(a, b)


def sqroot(a):
    if a < 0:
        raise ValueError("incorrect")
    return math.sqrt(a)
