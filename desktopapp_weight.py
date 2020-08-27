from tkinter import *

window = Tk()

def convert_wt():
	gram=float(e1_value.get())*1000
	pound=float(e1_value.get())*2.2
	oz=float(e1_value.get())*35.3
	t1.delete("1.0", END)
	t1.insert(END,gram)
	t2.delete("1.0", END)
	t2.insert(END,pound)
	t3.delete("1.0", END)
	t3.insert(END,oz)
	


l0=Label(window, text="kg")
l0.grid(row=0,column=0)

b1=Button(window,text="CONVERT", command=convert_wt)
b1.grid(row=0, column=2)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

l1=Label(window, text="gram")
l1.grid(row=1,column=0)

t1=Text(window, height=1, width=20)
t1.grid(row=2,column=0)
 
l2=Label(window, text="pound")
l2.grid(row=1,column=1)

t2=Text(window, height=1, width=20)
t2.grid(row=2,column=1)

l3=Label(window, text="oz")
l3.grid(row=1,column=2)

t3=Text(window, height=1, width=20)
t3.grid(row=2,column=2)

window.mainloop()
