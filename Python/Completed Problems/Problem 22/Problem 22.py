import string

with open("names.txt") as names:
    for line in names:
        Names = line.lower().replace('"', '').replace("'", '').split(',')
Names.sort()

def nameScore(name):
    """
    Returns the portion of a name's score from the letters that comprise it
    """
    LetterScore = dict(zip(string.ascii_lowercase, range(1,27)))
    nameScore = 0
    for letter in name:
        nameScore += LetterScore[str(letter)]
    return nameScore

TotalScore = 0

print("Colin is at position {}".format(Names.index("colin") + 1))

for index, name in enumerate(Names):
    TotalScore += (index + 1) * nameScore(name)

print("Total Score is {}".format(TotalScore))

