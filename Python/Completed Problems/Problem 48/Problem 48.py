sum = 0
for i in range(1,1001):
    sum += i**i

sum_string = str(sum)
print(sum_string[-10:])
