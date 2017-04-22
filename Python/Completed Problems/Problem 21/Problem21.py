def sumProperDivisors(number):
    """
    Takes an integer number, returns the sum of its proper divisors
    """
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum

def main(low, high):
    sumPropDiv = [sumProperDivisors(i) for i in range(low, high + low)]
    amicableNumbers = []
    for i in range(high - low + 1):
        index = sumPropDiv[i]
        try:
            if sumPropDiv[index - low] == i + low and (i + low) != index:
                amicableNumbers.extend([i + low, index])
        except IndexError:
            pass
    amicableNumbersSet = set(amicableNumbers)
    print("Answer is {}".format(sum(amicableNumbersSet)))
    return

if __name__ == '__main__':
    main(1,10000)
