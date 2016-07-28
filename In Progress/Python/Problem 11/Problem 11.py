matrix = []
with open("numbers.txt") as fileText:
    for line in fileText:
        matrix.append(list(map(int,line.split(" "))))

def max_product(xNum, yNum, matrix):
    """
    Num is the index of a number in the matrix
    max_product calculates the max product of four consecutive numbers
    along the horizontal with num  serving as the rightmost element,
    calculates along the vertical with num  serving as the bottommost element,
    and along the diagonal, with num serving as the right and bottommost
    element
    """
    horizontal = 1
    vertical = 1
    diagonal = 1
    for x in range(num - 4, num, -1):
        horizontal *= matrix[num