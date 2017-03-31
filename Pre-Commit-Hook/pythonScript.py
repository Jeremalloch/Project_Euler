import collections
from os import walk, path


rootPath = '/Users/jeremymalloch/Projects/Project_Euler'
pythonInProgress = list(walk(path.join(rootPath,'Python/In Progress')))[0][1]
pythonCompleted = list(walk(path.join(rootPath,'Python/Completed Problems')))[0][1]

CInProgress = list(walk(path.join(rootPath,'C/In Progress')))[0][1]
CCompleted = list(walk(path.join(rootPath,'C/Completed Problems')))[0][1]

HaskellInProgress = list(walk(path.join(rootPath,'Haskell/In Progress')))[0][1]
HaskellCompleted = list(walk(path.join(rootPath,'Haskell/Completed Problems')))[0][1]

Python = {problemName: "In Progress" for problemName in pythonInProgress}
for problemName in pythonCompleted:
    Python[problemName] = " Completed "

del Python["__pycache__"]

C = {problemName: "In Progress" for problemName in CInProgress}
for problemName in CCompleted:
    C[problemName] = " Completed "

Haskell = {problemName: "In Progress" for problemName in HaskellInProgress}
for problemName in HaskellCompleted:
    Haskell[problemName] = " Completed "

combinedDict = {} 
for k,v in Python.items():
    combinedDict[k] = (v,11*' ',11*' ')

for k,v in C.items():
    try:
        combinedDict[k] = (combinedDict[k][0],v,11*' ')
    except KeyError:
        combinedDict[k] = (11*' ',v,11*' ')

for k,v in Haskell.items():
    try:
        combinedDict[k] = (combinedDict[k][0],combinedDict[k][1],v)
    except KeyError:
        combinedDict[k] = (11*' ',11*' ',v)

newCombinedDict = {}
for key in combinedDict:
    newKey = '00' + key.rsplit(sep=' ',maxsplit=1)[-1]
    newKey = 'Problem ' + newKey[-3:]
    newCombinedDict[newKey] = combinedDict[key]

sortedDict = collections.OrderedDict(sorted(newCombinedDict.items()))

for k,v in sortedDict.items():
    print("|{}|{}|{}|{}|".format(k,v[0],v[1],v[2]))
