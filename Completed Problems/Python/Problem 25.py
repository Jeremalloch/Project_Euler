import math

index = 1
fibonacci = 1

while fibonacci < 10**999:
    index +=1
    fibonacci = (((1+math.sqrt(5))/2)**index)/math.sqrt(5)
print index