matrix = []
with open("numbers.txt") as fileText:
    for line in fileText:
        matrix.append(list(map(int, line.split(" "))))


def local_max_product(xNum, yNum):
    """
    Num is the index of a number in the matrix
    local_max_product calculates the max product of four consecutive numbers
    along the horizontal with num  serving as the rightmost element,
    calculates along the vertical with num  serving as the bottommost element,
    and along the diagonal, with num serving as the right and bottommost
    element
    It returns the maximum of these values
    """
    horizontal = 1
    vertical = 1
    diagonal = 1
    for x in range(4):
        horizontal *= matrix[xNum + x][yNum]
        vertical *= matrix[xNum][yNum + x]
        diagonal *= matrix[xNum + x][yNum + x]

    return max(horizontal, vertical, diagonal), xNum, yNum


def main():
    max_product = (0,0,0)
    temp = 0
    for xNum in range(17):
        for yNum in range(17):
            temp = local_max_product(xNum, yNum)
            if temp[0] > max_product[0]:
                max_product = temp
    print("Max product is {}".format(max_product[0]))
    print("Max product numbers start on {} situated at ({},{})".format(matrix[max_product[1]][max_product[2]],
                                                                       max_product[1], max_product[2]))
    return

if __name__ == '__main__':
    main()
