import math

primeFactors=[]
startingNum = 13195
currentNum = 13195

def primeFactor (num):
    """Factors a number by its lowest prime factor"""   
    for x in xrange(2,int(math.sqrt(num))):
        if num%x==0:
            return x
    return num

returnValue = 1
while returnValue != currentNum:
    currentNum /= returnValue
    returnValue = primeFactor(currentNum)
    primeFactors.append(returnValue)

print(primeFactors)

#Verification answer is true
product = 1
for prime in primeFactors:
    product*=prime

if product == startingNum:
    print("Product is equal to startingNum")
'''
def divisibleBy(num):
    """Returns a list of numbers a number is divisible by"""
    divisibleBy=[]
    for x in range(1,num+1):
        if num%x == 0:
            divisibleBy.append(x)
    return divisibleBy

for prime in primeFactors:
    print(prime)
    print(" is divisible by ")
    print(divisibleBy(prime))

'''
        