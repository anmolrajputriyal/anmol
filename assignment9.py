#Q1
class circle():
    def __init__(self,r):
     self.radius=r
    def getarea(self):
        return self.radius**2*3.14
    def getcircumference(self):
        return 2*self.radius*3.14
x=circle(4)
print("area of circle:",x.getarea())
print("circumference of circle:",x.getcircumference())

#Q2
class student():
    def __init__(self,name,rollno):
        self.n=name
        self.r=rollno
x=student('Anmol',7)
print("name is:",x.n)
print("roll number is:",x.r)

#Q3
class temperature():
    def __init__(self,celsius_temp):
        self.c=celsius_temp
    def fahrenheit(self):
        return 9/5*self.c+32
    def celcius(self):
        return self.c
x=temperature(37.5)
print("degree fahrenheit", x.fahrenheit())
print("ss",x.celsius())

#Q5
class expenditure():
    def __init__(self,expenditure,total_saving,total_salary=0):
        self.exp=expenditure
        self.s=total_saving
        self.t=0
    def display(self):
        print("total expenditure:",self.exp)
        print("total saving:",self.s)
    def total_salary(self):
        self.t=self.exp+self.s
    def display_salary(self):
        return self.t
user_input=int(input("enter the expenditure"))
user_input1=int(input("enter saving"))
x=expenditure(user_input,user_input1)
x.display()
x.total_salary()
print("total salary:",x.display_salary())
