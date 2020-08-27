from tkinter import *

from tkinter import messagebox

import Fixture_app_backend

"""
A program that saves fixture information
Date of test, Project, Package Code, Fixture Used, Remarks
"""

def get_selected_row(event):
	global selected_row
	index=list1.curselection()[0]
	selected_row=list1.get(index)
	e0.delete(0, END)
	e0.insert(END, selected_row[1])
	e1.delete(0, END)
	e1.insert(END, selected_row[2])
	e2.delete(0, END)
	e2.insert(END, selected_row[3])
	e3.delete(0, END)
	e3.insert(END, selected_row[4])
	e4.delete(0, END)
	e4.insert(END, selected_row[5])
	e5.delete(0, END)
	e5.insert(END, selected_row[6])
	e6.delete(0, END)
	e6.insert(END, selected_row[7])
	e7.delete(0, END)
	e7.insert(END, selected_row[8])
	e8.delete(0, END)
	e8.insert(END, selected_row[9])
	e9.delete(0, END)
	e9.insert(END, selected_row[10])
	

def view_command():
	list1.delete(0,END)
	for row in Fixture_app_backend.view():
		list1.insert(END, row)

def search_command():
	list1.delete(0, END)
	for row in Fixture_app_backend.search(Dt.get(), Project_text.get(), Package_text.get(), Model_text.get(), Test_text.get(), Shaker_text.get(), FixZ_text.get(), FixXY_text.get(), Coordinate_text.get(), Remarks_text.get()):
		list1.insert(END, row)
	
def add_command():
	Fixture_app_backend.insert(Dt.get(), Project_text.get(), Package_text.get(), Model_text.get(), Test_text.get(), Shaker_text.get(), FixZ_text.get(), FixXY_text.get(), Coordinate_text.get(), Remarks_text.get())
	list1.delete(0, END)
	view_command()
	print("you added a new row")
	

def update_command():
	result=messagebox.askyesno("WARNING!", "UPDATE selected row?")
	if result is True:
		print("you updated a row with id=", (selected_row[0]))
		Fixture_app_backend.update(selected_row[0], Dt.get(), Project_text.get(), Package_text.get(), Model_text.get(), Test_text.get(), Shaker_text.get(), FixZ_text.get(), FixXY_text.get(), Coordinate_text.get(), Remarks_text.get())
		list1.delete(0, END)
		view_command()
	else:
		pass
	
def delete_command():
	result=messagebox.askyesno("WARNING!", "DELETE selected row?")
	if result is True:
		print("you deleted a row with id=", (selected_row[0]))
		Fixture_app_backend.delete(selected_row[0])
		list1.delete(0, END)
		view_command()
	else:
		pass
	

	
window=Tk()

window.wm_title("Fixture Database")

l0=Label(window, text="Date of Test", anchor="e", width=20)
l0.grid(row=0,column=0)

Dt=StringVar()
e0=Entry(window,textvariable=Dt, width=20)
e0.grid(row=0,column=1)

l1=Label(window, text="Project", anchor="e", width=20)
l1.grid(row=0,column=2)

Project_text=StringVar()
e1=Entry(window,textvariable=Project_text, width=20)
e1.grid(row=0,column=3)

l2=Label(window, text="Package Code", anchor="e", width=20)
l2.grid(row=0,column=4)

Package_text=StringVar()
e2=Entry(window,textvariable=Package_text, width=20)
e2.grid(row=0,column=5)

l3=Label(window, text="Model", anchor="e", width=20)
l3.grid(row=1,column=0)

Model_text=StringVar()
e3=Entry(window,textvariable=Model_text, width=20)
e3.grid(row=1,column=1)

l4=Label(window, text="Test Philosophy", anchor="e", width=20)
l4.grid(row=1,column=2)

Test_text=StringVar()
e4=Entry(window,textvariable=Test_text, width=20)
e4.grid(row=1,column=3)

l5=Label(window, text="Shaker", anchor="e", width=20)
l5.grid(row=1,column=4)

Shaker_text=StringVar()
e5=Entry(window,textvariable=Shaker_text, width=20)
e5.grid(row=1,column=5)

l6=Label(window, text="Fixture for Out-of-Plane", anchor="e", width=20)
l6.grid(row=2,column=0)

FixZ_text=StringVar()
e6=Entry(window,textvariable=FixZ_text, width=20)
e6.grid(row=2,column=1)

l7=Label(window, text="Fixture for in-Plane Axis", anchor="e", width=20)
l7.grid(row=2,column=2)

FixXY_text=StringVar()
e7=Entry(window,textvariable=FixXY_text, width=20)
e7.grid(row=2,column=3)

l8=Label(window, text="Coordinate", anchor="e", width=20)
l8.grid(row=2,column=4)

Coordinate_text=StringVar()
e8=Entry(window,textvariable=Coordinate_text, width=20)
e8.grid(row=2,column=5)

l9=Label(window, text="Remarks", anchor="e", width=20)
l9.grid(row=3,column=0)

Remarks_text=StringVar()
e9=Entry(window,textvariable=Remarks_text, width=67)
e9.grid(row=3,column=1, columnspan=3)

list1=Listbox(window, height=10, width=93)
list1.grid(row=4,column=0,rowspan=6,columnspan=4, pady=5)

list1.bind('<<ListboxSelect>>', get_selected_row)

sby1=Scrollbar(window, orient="vertical")
sby1.grid(sticky=W, row=4, column=4,rowspan=6)

list1.configure(yscrollcommand=sby1.set)
sby1.configure(command=list1.yview)

sbx1=Scrollbar(window, orient="horizontal")
sbx1.grid(row=10, column=0,columnspan=4)

list1.configure(xscrollcommand=sbx1.set)
sbx1.configure(command=list1.xview)

b1=Button(window, text="View All", width=16, command=view_command)
b1.grid(row=4, column=5)

b2=Button(window, text="Search", width=16, command=search_command)
b2.grid(row=5, column=5)

b3=Button(window, text="Add", width=16, command=add_command)
b3.grid(row=6, column=5)

b4=Button(window, text="Update", width=16, command=update_command)
b4.grid(row=7, column=5)

b5=Button(window, text="Delete", width=16, command=delete_command)
b5.grid(row=8, column=5)

b6=Button(window, text="Close", width=16, command=window.destroy)
b6.grid(row=9, column=5)

window.mainloop()