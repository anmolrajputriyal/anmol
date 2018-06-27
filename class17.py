'''import tkinter
top=tkinter.Tk()
top.title("rajput")
top.geometry("700x700")

btn=tkinter.Button(top,text="click",command="hello")
btn.pack()
top.mainloop()

from tkinter import *
master=Tk()
w=Canvas(master,width=400,height=600)
w.pack()
canvas_height=20
canvas_width=200
y=int(canvas_height/2)
w.create_line(0,y,canvas_width,y)
mainloop()

from tkinter import *
master=Tk()
var1=IntVar()
Checkbutton(master,text='male',variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(master,text='female',variable=var2).grid(row=1,sticky=W)
mainloop()

from tkinter import *
master=Tk()
Label(master,text='first name').grid(row=0)
Label(master,text='last name').grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
mainloop()
'''
from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton=Button(frame,text='red',fg='red')
redbutton.pack(side=LEFT)
greenbutton= Button(frame,text='brown',fg='brown')
greenbutton.pack(side=LEFT)
bluebutton=Button(frame,text='blue',fg='blue')
bluebutton.pack(side=LEFT)
root.mainloop()