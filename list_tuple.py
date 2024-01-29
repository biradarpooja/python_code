"""lis=[153,121,23,543,56,46]
tupl=()
se={1}
dic={1:'pooja'}
print(type(lis))
print(type(tupl))
print(type(se))
print(type(dic))
print(lis)"""
"""
for i in range(4)
    i=i+1
    print(lis[i])"""
"""
for i in lis:
    if i%2==0:
        print(i,"num is even")
    if i%2==1:
        print(i,"num is odd")
        """
'''#write a code armstrong num
for num in lis:
    rem=0
    add=0
    temp=num
while num>0:
         rem=num%10
         add =(rem**3)+add
         num=num//10
if temp==add:
    print(temp,"is armstrong number")
else:
    print(temp,"is not armstrong num")'''
"""#write a code pellindrome
for num in lis:
    rem=0
    add=0
    temp=num
    while num>0:
       rem=num%10
       add =(add*10)+add
       num=num//10
    if temp==add:
        print(temp,"is pellindrome number")
    else:
        print(temp,"is not pellindrone num")"""
"""
lis.append(100)
print("after adding element",lis) #100-argument,lis-class ,append-object"""
student=[]
for i in range(2):
       name=str(input("enter student name "))
       student.append(name)
print("student name",student)
for i in range(1):
       pos=int(input("enter position"))
       name=str(input("enter name"))
       student.insert(pos,name)
print("after inserting student",student)
for i in range(1):
       #student.clear()
       #print(student)
       student.copy()
       print(student)
       #student.count()
       #print(student)

        

