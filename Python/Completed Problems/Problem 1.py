multipleOfThree=[]
multipleOfFive=[]

#finding multiples of three
for x in xrange(0,335):
    if x*3 < 1000:
         multipleOfThree.append(x*3)

for x in xrange(0,202):
    if x*5 <1000 :
       multipleOfFive.append(x*5)

for x in multipleOfFive:
    for y in multipleOfThree:
        if x == y:
            multipleOfThree.remove(x)
  
sum = 0

for x in multipleOfThree:
    sum+=x

for x in multipleOfFive:
    sum+=x
    
print(sum)

//hi