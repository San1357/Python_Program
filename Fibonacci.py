def Fibonacci(n):
    if n<0:
       print ("INcorrect input")
# because First Fiboacci number is 0
    elif n==1:
         return 0
# because Second Fibonacci number is 1
    elif n==2:
         return 1
    else:
         return Fibonacci(n-1)+Fibonacci(n-2)


print(Fibonacci(9))

