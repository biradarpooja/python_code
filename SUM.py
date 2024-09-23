'''
#rectangle
l=int(input("Enter length"))
b=int(input("Enter breadth"))
area_rec=((l*b))
print("Area of rec",area_rec)'''
'''
#roll number name and percentage
roll_num=int(input("Enter student Roll number"))
name=input("Enter student name")
per=float(input("Enter student percetage"))
print("Student roll number is ",roll_num,"name is",name,"percetage is ",per)'''
'''
student=[]
for i in range(5):
       name=str(input("enter student name "))
       student.append(name)
print("student name",student)'''
'''for i in range(10):
    if i%2==1:
        print(i,"is odd Number")
        sum1=sum1+1
print("sum is",sum1)'''
import pandas as pd
city={"pune":[34,43,54,54,54,34,43],
      "latur":[43,43,54,54,65,34,24],
      "solapur":[32,43,54,65,65,76,65],
      "kolhapur":[32,54,65,34,75,54,34]}
ds=pd.DataFrame(city,index=["sunday","munday","Tuesday","wednesday","thursday","Friday","satardayu"])
print(ds)


    
