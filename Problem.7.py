import math

def isPrime(number, primeList):
    """returns a bool if a number is prime or not"""
    primeStatus = True
    for x in primeList:
        if number%x==0:
            return False
    return True


primes = [2]
currentNumber=3
numPrimes=1

while numPrimes < 10001:
    primeFound=False
    while primeFound == False:
        if isPrime(currentNumber, primes):
            primes.append(currentNumber)
            primeFound=True
        currentNumber+=1
    numPrimes+=1

print(primes[10000])