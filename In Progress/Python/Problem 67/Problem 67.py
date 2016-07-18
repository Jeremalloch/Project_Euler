import copy
triangle = []
with open("Triangle.txt") as TriangleFile:
    for line in TriangleFile:
        triangle.append(list(map(int, line.split(" "))))

positionCost = copy.deepcopy(triangle)
for rowIndex in range(1, len(triangle)):
    for columnIndex in range(1, len(triangle[rowIndex]) - 1):
        positionCost[rowIndex][columnIndex] += max(positionCost[rowIndex - 1][columnIndex - 1], positionCost[rowIndex - 1][columnIndex])
    positionCost[rowIndex][0] += positionCost[rowIndex - 1][0]
    positionCost[rowIndex][-1]+= positionCost[rowIndex - 1][-1]

maxTotal = max(positionCost[-1])
print("Maximum total from top to bottom is {}".format(maxTotal))
