import time

start_time = time.time()


found = False

num = 0

while (found == False):
    num+=1
    divisor = 20
    zeroRemainder = True
    while(divisor > 10 and zeroRemainder):
        if (num%divisor == 0):
            divisor+=1
        else:
            zeroRemainder = False
        #print divisor
        #print zeroRemainder
    if (zeroRemainder):
        found = True
    #print "Num is now:"
    #print num
print "Final number is:"
print num

elapsed_time = time.time() - start_time

print elapsed_time