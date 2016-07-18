matrix = []
with open("numbers.txt") as fileText:
    for line in fileText:
        matrix.append(list(map(int,line.split(" "))))

