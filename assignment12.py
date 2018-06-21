#Q1
#it is zero division error
'''
class handle(Exception):
    pass
try:
    a=3
    if(a<4):
        a=a/(a-3)
        raise handle
except ZeroDivisionError:
    print("it cannot be divisible by zero it will give zero division error")

#Q2
#it is index error
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("enter correct index value")

#Q3
#an Exception

#Q4
#-5.0
#a/b result in 0

#Q5
try:
    import anmol
except ImportError:
    print("enter a valid import file")
try:
    import threading
except ImportError:
    print("enter a valid import file")
try:
    a=int(input("enter the number"))
except ValueError:
    print("enter a integer number")
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("enter correct index value")
try:
    l=[1,2,3]
    print(l[2])
except IndexError:
    print("enter correct index value")
'''
#Q6
class Age(Exception):
    pass
a=int(input("enter age"))
try:
    a=int(input("enter the age"))
    if(a>17):
        print(a)
    else:
        raise Age()
except Age():
    print("age is less than 18")
