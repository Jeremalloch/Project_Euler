numberList = []
with open("number.txt") as numberFile:
    for line in numberFile:
        numberList.append(line.rstrip())
numberString = "".join(numberList)

maxProduct = 0
tempProduct = 0
for index in range(len(numberString) - 12):
    tempProduct = 1
    for i in range(13):
        tempProduct *= int(numberString[index + i])
    if tempProduct > maxProduct:
        maxProduct = tempProduct
print("The max product is {}".format(maxProduct))
