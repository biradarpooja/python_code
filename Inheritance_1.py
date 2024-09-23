#LINE SLOpe DISTANCE
'''class line:
     def Slope(self,x1,x2,y1,y2):
         slp=(y2-y1)/(x2-x1)
         return slp
         
     def dist(self,a,b,c,d):
         dis=((a-b)**2 + (c-d)**2)**0.5
         print(dis)
class show(line):
    def info(self):
        print(line.Slope(self,2,3,4,5))
my=show()
my.info()
'''
#class 1 method one globle variable make anoter method and double and make another ans
#+10 make another divide 2 all is globle
"""class Number:
    def Num1(self,a):
        print("Initial Value is:",a)
    def Num2(self,a):
        print("Double value is:",a*2)
    def Num3(self,a):
        print("+10 value is:",a+10)
    def Num4(self,a):
        print("/2 value is:",a/2)
class show(Number):
    def info(self):
        print(show.Num1(self,a))
        print(show.Num2(self,a))
        print(show.Num3(self,a))
        print(show.Num4(self,a))     
a=int(input("Enter Initial Value"))
my=show()
my.info()"""
class Number:
    a=0
    def double(self,x):
        self.a=x*2
        print(self.a)
    def plusten(self):
        self.a=self.a+10
        print(self.a)
        
    def half(self):
        self.a=(self.a)/2
        return self.a
num=Number()
i=int(input("Enter any number"))
num.double(i)
num.plusten()
print(num.half())


