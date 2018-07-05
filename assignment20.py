#Q1
'''import pandas as pd
data={'Name':['anmol','abhi','aditya','rahul',],'Age':[20,22,21,20],'mail id':['evf.g@gmail.com','ghdhej.e@gmail.com',
'djadj.b@gmail.com','addd.s@gmail.com'],'phone number':[998876689,8769999766,865788998,335569869]}
df=pd.DataFrame(data)
print(df)
'''
#Q2
import pandas as pd
data=pd.read_csv("datasheet.csv")
df=pd.DataFrame(data)
print(df)
print(df.head(5))
print(df.head(10))
print(df.shape)
print(df.axes)
print(df.sum())
print(df.describe())
print(df.size)
print(df.dtypes)
print(df.tail(5))
print("2nd column MinTemp:")
print(df['MinTemp'])
print(df['MinTemp'].shape)
print(df['MinTemp'].sum())
print(df['MinTemp'].describe())
print(df['MinTemp'].count())
print(df['MinTemp'].axes)
print(df['MinTemp'].mean())
print(df['MinTemp'].size)
print(df['MinTemp'].dtypes)


