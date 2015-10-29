# -*- coding: utf8 -*-
"""
Using the Python language, have the function FirstFactorial(num) take the num parameter being passed
and return the factorial of it (ie. if num = 4, return (4 * 3 * 2 * 1)).
For the test cases, the range will be between 1 and 18.
"""


def first_factorial(num):

    try:
        num = int(num)
    except ValueError:
        return 'Please enter an integer'

    if num < 1 or num > 18:
        return 'This number is not between 1 and 18'
    else:
        r = range(1, num + 1)
        return reduce(lambda x, y: x*y, r)

print(first_factorial(raw_input()))
