# ARMSTRONG Number= https://www.youtube.com/watch?v=fdxtmMOfdrc ( very good Explanation)
# Example : 

/*Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9

Input : 1634
Output : Yes
1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
*/

# Formula abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 

# CODE:

a= int(input("enter the number till where u want the armstrong no"))
for i in range(a):
     num = i 
     result = 0
     n=len(str(i))            # here n is equal to no. of digit in given no.
     while(i!=0):
         digit = i % 10
         result = result+digit**n
         i = i//10           
     
     if (num == result):
            print(num)
            print (" are Armstrong number")

