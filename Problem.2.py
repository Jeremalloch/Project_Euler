Fibonacci = [1,1,2]

sum = 0
 
n=2
while Fibonacci[n] <= 4000000:
    Fibonacci.append(Fibonacci[n] + Fibonacci[n-1])
    n+=1

for item in Fibonacci:
    if item <= 4000000 and item%2 == 0:
        sum+=item

print(Fibonacci)
print(sum)