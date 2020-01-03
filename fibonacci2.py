FibNo = [0,1]

def fibonacci(n):
    if n<0:
       print ("Incorrect Input ")
    elif n<=len(FibNo):
       return FibNo[n-1]
    else:
         temp_fib = fibonacci(n-1)+fibonacci(n-2)
         FibNo.append(temp_fib)
         return temp_fib


print (fibonacci(2))
