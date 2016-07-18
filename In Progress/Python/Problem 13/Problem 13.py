sum = 0
with open("numbers.txt") as numbersFile:
    for line in numbersFile:
        sum += int(line)

print("First 10 digits is {}".format(str(sum)[:10]))
