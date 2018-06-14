#Q1
keyboard=(2,5,7,'Anmol','Rajput')
print(len(keyboard))

#Q2
numbers=(2,4,55,8,7,9)
print(max(numbers))
print(min(numbers))

#Q3
tuple_elements=(1*2*4*5*6*7)
print(tuple_elements)

#Q4
#1 calculate difference between two sets.
set_a=set([1,2,3,5,7])
set_b=set([55,7])
set_final=set_a-set_b
print(set_final)

#2
set_a=set((1,2,3,4,5,6,7))
set_b=set((2,3,5,7))
set_c=set_a>=set_b
set_d=set_a<=set_b
print(set_c)
print(set_d)

#5
set_e=set_a&set_b
print(set_e)

#Q6
user_name=input("enter the name")
user_age=input("enter your age")
user_data={'name':user_name,'age':user_age}
print(user_data)

#Q7
keyword=("MISSISSIPPI")
check_m=keyword.count("M")
check_i=keyword.count("I")
check_s=keyword.count("S")
check_p=keyword.count("P")
keyword_result={'numbers of M':check_m,'numbers of I':check_s,'numbers of S':check_s,'numbers of P':check_p,}
print(keyword_result)
