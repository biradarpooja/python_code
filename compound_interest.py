#write a code compound interest
p=int(input("Enter the principle amount"))
r=int(input("Enter the rate:"))
t=int(input("Enter the time:"))
i=1
while i<=t:
    si=(p*r)/100
    p=si+p
    print("after ",i,"year",p,"amount")
    i=i+1
print("final amount is",p)
