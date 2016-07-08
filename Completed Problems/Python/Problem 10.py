import math
import time
start_time = time.time()


def  findPrimes (target):
    '''
    Function returns a list of all primes below the target
    '''
    
    firstPrimes = [2,3,5,7] #Primes less than 10
    secondPrimes = [] #Larger list of primes
    level = 10 #Current value that all primes below have been calculated for
    
    #Growing the level exponentially, the level is squared after each loop through here
    #It is cut off at sqrt(target) so as not to compute unnecessary primes above the target
    while level < math.sqrt(target):
        for num in xrange(level, level**2): #excludes primes**2, which will be even and not prime
            if num%2 != 0: # if the number is even, it will not be prime
                Prime = True
                for prime in firstPrimes:
                    if num%prime == 0: #if the number is divisible by any of the prexisting primes, it is not a prime
                        Prime = False
                if Prime:
                    secondPrimes.append(num) #if the number is not divisible by any of the existing primes, it is a prime, and is added to the second list of primes
        firstPrimes += secondPrimes
        secondPrimes = []
        level = level**2
    
    #Last loop through the prime sieve, which cuts off when the target is hit
    if target > level:  
        for num in xrange(level+1, target+1):
            if num%2 != 0: # if the number is even, it will not be prime
                Prime = True
                for prime in firstPrimes:
                    if num%prime == 0: #if the number is divisible by any of the prexisting primes, it is not a prime
                        Prime = False
                if Prime:
                    secondPrimes.append(num) #if the number is not divisible by any of the existing primes, it is a prime, and is added to the second list of primes
        firstPrimes += secondPrimes
    
    #removing primes above the target if the target is less than 10
    if target < 7:
        for prime in firstPrimes:
            if prime > target:
                firstPrimes.remove(prime)

    return firstPrimes
    
PrimesUnder2K = findPrimes(2*10**6) #Create a list of all primes less than or equal to 2 million
sumOfPrimes = 0 #sum of all the primes from the list generated in the step before

for prime in PrimesUnder2K:
    sumOfPrimes+=prime #Adding up the primes from the list into an integer
print(sumOfPrimes)

print("--- %s seconds ---" % (time.time() - start_time)) #Prints out to time to compute the code