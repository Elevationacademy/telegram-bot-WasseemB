import math
import database


def is_prime(number):
    if number == 1:
        return True
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True


def is_palindrome(s):
    return s[::-1] == s


def sqrt(number):
    return math.sqrt(number)


def is_fact(number):
    fact_table = [1, 2, 4, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 3.991680e7, 4.790016e8, 6.227021e9,
                  8.717829e10, 1.307674e12, 2.092279e13, 3.556874e14, 6.402374e15, 1.216451e17, 2.432902e18]
    if number == 1:
        return True
    elif number % 2 != 0:
        return False
    elif number in fact_table:
        return True
    return False


def popular(a):
    return database.read_popular()
