# take an input year from user and decide whether it is a leap year or not.
z=int(input("enter year"))
if(z%4==0):
    print("the year is leap")
else:
    print("the year is not leap")

# take the length and breadth input from user and chech whether the dimensions are of square and rectangle.
x=int(input("enter length"))
y=int(input("enter breadth"))
if(x==y):
    print("length and breadth is of square")
else:
    print("length and breadth is of rectangle")

# take the input age of 3 people and determine oldest and youngest among them.
a=int(input("enter age of first person"))
b=int(input("enter age of second person"))
c=int(input("enter age of third person"))
if(a>b>c):
    print("among all the three person a is oldest")
elif(b>a>c):
    print("among all the three person b is oldest")
elif(c>a>b):
    print("among all the three person c is oldest")
if(a<b<c):
    print("among all the three person a is youngest")
if(b<a<c):
    print("among all the three person b is youngest")
if(c<a<b):
    print("among all the three person c is youngest")
else:
    print("two person have same age")

#Q4
r=int(input("enter the points which is scored"))
if(r>=1 and r<=50):
    print("no prize won")
elif(r>=51 and r<=150):
    print("won wooden dog in a prize")
elif(r>=151 and r<=180):
    print("won book in a prize")
else:
    print("won chocolates in prize")
#Q5
i=int(input("enter the quantity"))
price=i*100
if(price>1000):
    print(price=0.10*price)
else:
    print(price)


