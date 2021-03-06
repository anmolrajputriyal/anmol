#Q1
import sqlite3
conn=sqlite3.connect('data.db')
print("database created successfully")
conn.execute('''CREATE TABLE BOOKS (BOOK_ID INT PRIMARY KEY NOT NULL,TITLE_ID TEXT NOT NULL,LOCATION TEXT NOT NULL,
GENRE_ID TEXT NOT NULL);''')
conn.execute("INSERT INTO BOOKS(BOOK_ID,TITLE_ID,LOCATION,GENRE,)VALUES(11023, '25893', 32, 'california', 20000.00)")
conn.execute('''CREATE TABLE TITLE(TITLE_ID INT NOT NULL,TITLE_NAME TEXT NOT NULL,ISBN INT NOT NULLPUBLISHER_IDINT NOT
NULL,PUBLISHER_YEAR INT NOT NULL);''')
conn.execute('''CREATE TABLE PUBLISHERS(PUBLISHER_ID INT NOT NULL,NAME TEXT NOT NULL,STREET_ADDRESS CHAR(50),
SUITE_NUMBER INT NOT NULL,ZIP_CODE_ID INT NOT NULL);''')
conn.execute('''CREATE TABLE ZIPCODES(ZIP_CODE_ID INT NOT NULL,CITY TEXT NOT NULL,STATE TEXT NOT NULL,ZIP_CODE INT NOT
NULL);''')
conn.execute('''CREATE TABLE AUTHORSTITLES(AUTHORS_TITLES_ID INT NOT NULL,AUTHOR_ID INT NOT NULL,TITLE_ID INT NOT 
NULL);''')
conn.execute('''CREATE TABLE AUTHORS(AUTHOR_ID INT PRIMARY KEY NOT NULL,FIRST_NAME TEXT NOT NULL,MIDDLE_NAME TEXT NOT 
NULL,LAST_NAME TEXT NOT NULL);''')
print("table created successfully")
#Q2
import sqlite3
conn=sqlite3.connect('test.db')
print("opened database successfully")
conn.execute('''CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,ADDRESS CHAR(50),
SALARY REAL);''')
print("table created successfully")
conn.execute('''INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(1,'ANMOL',21,'CALIFORNIA',200000.00)''')
conn.execute('''INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(2,'ABHI',20,'CALIFORNIA',210000.00)''')
conn.commit()
print("inserted successfully")
#Q3
print("BEFORE UPDATING")
cursor=conn.execute("SELECT id,name,address,salary from COMPANY")
for row in cursor:
    print("ID=",row[0])
    print("NAME=",row[1])
    print("ADDRESS=",row[2])
    print("SALARY=",row[3],"\n")
print("AFTER UPDATING")
conn.execute("UPDATING COMPANY set SALARY=SALARY+10000 where AGE=21")
cursor=conn.execute("SELECT id,name,address,salary from COMPANY")
for row in cursor:
    print("ID=",row[0])
    print("NAME=",row[1])
    print("ADDRESS=",row[2])
    print("SALARY=",row[3],"\n")
print("records created successfully")


