#Q1
'''
def area(r):
    area=3.14*r*r
    return area
print(area(7))

#Q2
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        return True
    else:
        return False
for i in range(1,1001):
    if (perfect(i)):

#Q3
def table(n,t=1):
    if(t==11):
        return
    (print(str(n)+"x"+str(t)+"="+ str(n*t)))
    table(n,t+1)
table(n=12)

#Q4
def power(a,b):
    if(b==1):
        return a
    else:
        return(a*power(a,b-1))
    print(power(4,4))
'''
#Q5
n=int(input("enter the number to get the factorial"))
def fact(n):
    if n == 0:
        return 1
    s=n * fact(n-1)
    return s
b=fact(n)
d={n:b}
print(d)