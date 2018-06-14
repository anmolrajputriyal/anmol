#Q1 what is the time tuple?
print("there is a popular time module available in python which provides function for working with time,and for coverting"
      "between representation,the function (time.time()) returns the current system time in ticks since 12am,january"
      "1,1970(epoch)")

            #"index    Attribute     values"
            #"0        tm_year       2018"
            #"1        tm_mon        1-12"
            #"2        tm_mday       1-31"
            #"3        tm_hour       0 to 23"
            #"4        tm_min        0 to 59"
            #"5        tm_sec        0 to 61(60 or 61 are leap- seconds"
            #"6        tm_wday       0 to 6"
            #"7        tm_yday       1 to 366"
            #"8        tm_isdst      -1,0,1 where -1 means library determine DST")'''

#Q2
import time
print(time.asctime())

#Q3
import datetime
d=(datetime.date.today())
print(d.month)

#Q4
import datetime
d=(datetime.date.today())
print(d.day)

#Q5
import datetime
a='2024/02/10'
d=(datetime.datetime.strptime(a,"%y/%m/%d"))
print(d.day)

#Q6
import time
print(time.asctime(time.localtime()))

#Q7
import math
f=int(input("enter the number"))
print(math.factorial(f))

#Q8
import math
a=int(input("enter the number"))
b=int(input("enter the number"))
print(math.gcd(a,b))

#Q9
import os
print(os.getcwd())
print(os.environ)