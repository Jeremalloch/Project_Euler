import itertools

def nth(iterable, n):
    return next(itertools.islice(iterable, n, None), None)

answer = str(nth(itertools.permutations(range(10)), 10**6 - 1)).strip("()").replace(", ","")
range = [x for x in range(10)]
print("The millionth permutation of {} is {}".format(range, answer))
