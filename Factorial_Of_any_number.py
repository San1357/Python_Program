 # n! = n*(n-1)*(n-2)*(n-3)*............*1 this is Called FACTORIAL .
 
# Let's take Example suppose we have to find "FACTORIAL OF 5" ? 
# viz equal to 5*4*3*2*1 = 120

#CODE

def factorial(n):
     
     if (n==0 or n==1):
          return 1
     else :
          return n* factorial(n-1)
          
          
num = 6
print("Factorial of",num,"is", factorial(num)) 

#OUTPUT : 720
