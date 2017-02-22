def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def choose(n, r):
    """
    N choose R
    """
    return factorial(n)/(factorial(r)*factorial(n-r))

