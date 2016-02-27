def finalMoney(numWins, fValue):
    '''
    Returns the amount of money returned with a given number of wins and 
    a specific fValue (proportion of money being gambled with each turn, as a
    decimal). 
    '''
    return ((1+2*fValue)**numWins)*((1-fValue)**(1000-numWins)) - (10**9)

def fMDerivative(numWins, fValue):
    '''
    Derivative of the finalMoney function.
    '''
    return 2*numWins*((1+2*fValue)**(numWins-1))*((1-fValue)**(1000-numWins)) - ((1+2*fValue)**numWins)*(1000-numWins)*((1-fValue)**(999-numWins))

fValMin = 0
fValMax = 1
numWins = 1000

fMinTemp = fValMin + 1
fMaxTemp = fValMax + 1

#print fValMin
#print fMinTemp

#Find lower bound of fVal
#while (abs(fValMin-fMinTemp) > 10**-13):
##for x in range(2):
##    fMinTemp = fValMin
##    fValMin = fValMin - (finalMoney(1000,fValMin)/fMDerivative(1000, fValMin))
##    print fValMin
#    print fMinTemp
#print fValMin

#print (finalMoney(1000,fValMin)/fMDerivative(1000, fValMin))

print fMDerivative(1000,0.1)