#Q1
class Animals():
    def animal_attributes(self):
        print("tiger")
class tiger(Animals):
    def king(self):
        print("king of the jungle")
k=tiger()
k.animal_attributes()
k.king()
#Q2
#A B
#A B
#Q3
class cop:
    def __init__(self,name,age,work__experience,designation):
        self.name=name
        self.age=age
        self.work__experience=work__experience
        self.designation=designation
    def display(self):
        print("before update")
        print("name=",self.name)
        print("age=",self.age)
        print("work__experience=",self.work__experience)
        print("designation=",self.designation)
    def __update__(self,name,age,work__experience,designation):
        self.name=name
        self.age=age
        self.work__experience=work__experience
        self.designation=designation
class mission(cop):
    def add__mission_detail(self,name,age,work__experience,designation):
        print("updated cop details are")
        print("name=",end="")
        self.name=name
        print(name)
        print("age=",end="")
        self.age=age
        print(age)
        print("work experience=",end="")
        self.work__experience=work__experience
        print(work__experience)
        print("designation=",end="")
        self.designation=designation
        print(designation)
#Q4
class shape():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self,):
        area=self.length*self.breadth
        print("shape:",area)
class rectangle(shape):
    def area(self):
        area=self.length*self.breadth
        print("rectangle:",area)
class square(shape):
    def area(self):
        area=self.length*self.breadth
        print("square:",area)
x=rectangle(5,7)
y=square(2,2)
x.area()
y.area()




