#Q1
'''
f=open("file.txt",encoding="utf8")
a=(f.readlines())
a.reverse()
n=int(input("enter the number of lines that should be print"))
for i in range(0,n):
    print(a[i])
f.close()

#Q2
a="rajput"
f=open("file1.txt","r")
k=f.read()
m=k.split()
print(k.count(a))

#Q3
f=open("file.txt",encoding="utf8")
a=(f.readlines())
c=open("file2.txt","w")
c.writelines(a)

#Q4
i=0
f=open("file2.txt",encoding="utf8")
a=(f.readlines())
b=open("file4.txt",encoding="utf8")
c=(b.readlines())
d=open("file3.txt","w")
for i,j in zip(a,c):
    d.write(i+j)
f.close()
b.close()
d.close()
'''
#Q5
l=[]
import random
import pickle
for i in range(0,10):
    l.append(random.randint(l,20))
f=open("file2.txt","w")
pickle.dump(l,f)