import re
#Q1
email=["zuck26@facebook.com","page23@google.com","jeff42@amazon.com"]
ls=[]
for i in email:
    a=re.findall("[\w]+",i)
    a=tuple(a)
    ls.append(a)
print(ls)

#Q2
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
name=re.findall("[b,B][a-z][A-Z]{1,5}",text)
print(name)

#Q3
sentence = "A, very very; irregular_sentence"
print(sentence)
a=re.compile("[,;_]")
for i in sentence:
    b=a.sub(" ",sentence)
print(b)