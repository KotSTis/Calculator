import math


def add(a, b=0):
    return a + b


def subtract(a, b=0):
    return a - b


def multiply(a, b=1):
    return a * b


def divide(a, b=1):
    return a / b


def absolute(a):
    return abs(a)


def inverse(a):
    if a == 0:
        return 0
    else:
        return 1 / a
