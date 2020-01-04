#  1**3 + 2**3 + 3**3 + ................ + n**3.

#CODE:


n = int(input("Enter the no.till where u want to find the cube of sum natural number:"))
sum = 0

for i in  range(1,n):
    sum += pow(i,3)
    print (sum)
print ("The sum of cube of natural number is:",sum)
     
     
     
     
