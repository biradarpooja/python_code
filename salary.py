#write a code if salary is more than 50k then increase 20% and otherwise increase 30%
a=int(input("Enter Employee Salary"))
if a>50000:
    new_salary=(a*20)/100
    final=new_salary+a
    print("employee incremented salary by 20% is:",final)
else:
    new_salary=(a*30)/100
    final=new_salary+a
    print("Employee incrememted salary by 30% is ",final)
