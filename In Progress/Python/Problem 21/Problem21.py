import math
from collections import Counter
import timeit

__author__ = 'Jeremy Malloch'


def sum_proper_divisors(number):
    """
    Takes an integer number, returns the sum of its proper divisors
    """
    sum = 0
    for i in range(1,number):
        if number % i == 0:
            sum += i
    return sum


def main():
    # Work in progress lol
    sum_proper_divisors_list = []
    for j in range(10001):
        sum_proper_divisors_list.append(sum_proper_divisors(j))
    amicable_numbers = []
    for number in sum_proper_divisors_list:
        if number <= 10000 and number == sum_proper_divisors_list[number]:
            amicable_numbers.append(number)
    return amicable_numbers


    # sum_of_amicable_numbers = 0
    # for key, value in frequency.items():
    #     if value > 1:
    #         sum_of_amicable_numbers += int(key)
    # return sum(amicable_numbers)

if __name__ == '__main__':
    print(main())