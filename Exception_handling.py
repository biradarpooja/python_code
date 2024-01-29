"""try:
    a=int(input("Enter number:"))
    b=int(input("enter number:"))
    c=a+b
    print(c)
except Exception as k:
    print(k)
print("right code")"""
"""a=int(input("Enter the num"))
b=int(input("enter the num"))
try:

    c=a/b1
    print(c)
except Exception as k:
    print(k)
print("excelent")"""
# can not divided by 5
"""class pooja(Exception):
try:
    a=int(input("Enter the num"))
    b=int(input("enter the num"))
    c=a/b
    if b==5:
        raise pooja("can not divided by 5")
    print(c)
    
except Exception as k:
    print(k)
print("excelent")"""

# raise the user define exception if the user enter an invalide value
"""class In(Exception):
    "for invalid number"
try:
    a=int(input("Enter number:"))
    b=int(input("enter number:"))
    c=a+b
    print(c)
    if a<0 or b<0:
        raise In("INVALID NUMBER")
except Exception as k:
    print(k.__class__)
    print(k)
print("right code")"""
#constructor
'''
class In(Exception):
    "for invalid number"
    def __init__(self):
       print("Invalid number")
try:
    a=int(input("Enter number:"))
    b=int(input("enter number:"))
    c=a+b
    print(c)
    if a<0 or b<0:
        raise In
except Exception as k:
    print(k.__class__)
    print(k)
print("right code")'''
#write a code raise an exception if sum of two side of triangle is less than the third side
class In(Exception):
     def __init__(self):
          print("Not Triangle")
try:
    a=int(input("Enter 1st side of triangle"))
    b=int(input("Enter 2nd side of triangle"))
    c=int(input("Enter 3rd side of triangle"))
    if c>a+b or a>b+c or b>a+c:
         raise In
except Exception as k:
    print(k)
print("correct")
    

