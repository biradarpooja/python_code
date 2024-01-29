"""def mul():#unargumented
    a=10
    b=20
    print(a*b)
mul()"""
#argumented function
'''
def mul(a,b):
    print(a*b)
mul(10,20)'''
#return function
"""def mul(a,b):
    return a*b
    return a+b
val=mul(10,20)
print(val)"""

#write a function to print sum of any five number
'''
def sum(a,b,c,d,e):
    return a+b+c+d+e
a=int(input("Enter num 1:"))
b=int(input("Enter num 2:"))
c=int(input("Enter num 3:"))
d=int(input("Enter num 4:"))
e=int(input("Enter num 5:"))
sumn=sum(a,b,c,d,e)
print("Sum of 5 num is:",sumn)
num=sumn
rev=0
while num!=0:
    dig=num%10
    rev=rev*10+dig
    num//=10
print("reversed number",str(rev))'''
#area of circle using function
'''
pi=3.14
def area(r):
    return(pi*(r*r))
r=float(input("Enter redious of circle"))
areaofcir=area(r)
print("the area of circle is:",areaofcir)'''
#write a code to factor of any number using function
'''def factor(a):
    return a
num=int(input("Enter any number you want to factor of this number"))
if num%a==0:
    print(a)
else:
    print("No factorial num")'''
'''
def factor(num):
    i=1
    while i<=num:
        if num%i==0:
            print(i,"is factor of",num)
        i=i+1
a=int(input("Enter number"))
factor(a)'''
#write a code to find wether the number is a prime number or not using funnction
def prm(num):
    i=1
    count=0
    while i<=num:
        if num%i==0:
            count=count+1
        i=i+1
    return count
a=int(input("enter number"))
c=prm(a)
if c>a:
    print(a,"is not a prime number")
else:
    print(a,"is a prime number")








