import string

preComp = {"-1":0, "0":0, "1": 0, "2":1}


def RhoCost (upperBound, lowerBound, preComp):
    '''
    Helper function to compute cost
    '''
    try:
        return preComp[str(upperBound - lowerBound)] + lowerBound
    except:
        #Must find a value of theta to minimize the cost
        costN = 10**100 #Total cost of n, stored as a variable so it can be added to the dictionary
        costT = 0 #Temporary variable to store the cost computed at each step
        for theta in xrange(lowerBound, upperBound + 1):
            costT = theta + max(RhoCost(upperBound, theta+1, preComp), RhoCost(theta-1, lowerBound, preComp))
            if costT < costN:
                costN = costT
                preComp[str(upperBound)] = costN
        return costN

def Cost (n, preComp):
    '''
    Returns the worst case cost of searching between 1 and n
    preComp is a dictionary of precomputed values, enabling a dynamic programming
    solution, so that worst case runtime is O(n^2) (I think lol), not O(n!)
    '''
    return RhoCost(n, 1, preComp)    

Cost(8, preComp)
print(preComp)
#print(Cost(2, preComp))
#print(Cost(3, preComp))
#print(Cost(4, preComp))