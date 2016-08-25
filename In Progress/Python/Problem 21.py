import math
from collections import Counter
import timeit

__author__ = 'Jeremy Malloch'


def proper_divisors(number):
    """
    Takes an integer number, returns a list of its proper divisors
    """
    upper_stop = math.ceil(math.sqrt(number))
    divisors = [1]
    if number < 1:
        return []
    for i in range(2, upper_stop + 1):
        if number % i == 0:
            divisors.append(i)
            divisors.append(number//i)
    return divisors


def main():
    sum_proper_divisors = []
    for x in range(10001):
        sum_proper_divisors.append(sum(proper_divisors(x)))
    amicable_numbers = []
    for number in sum_proper_divisors:
        if number <= 10000 and number == sum_proper_divisors[number]:
            amicable_numbers.append(number)

    return amicable_numbers


    # sum_of_amicable_numbers = 0
    # for key, value in frequency.items():
    #     if value > 1:
    #         sum_of_amicable_numbers += int(key)
    # return sum(amicable_numbers)

if __name__ == '__main__':
    print(main())