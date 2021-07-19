import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is the function called when the button is clicked
def open_file():
	print('clicked')


# this is the function called when the button is clicked
def manual_mode():
	print('clicked')


# this is the function called when the button is clicked
def auto_mode():
	print('clicked')


# this is a function to get the selected radio button value
def getRadioButtonValue():
	buttonSelected = Yes.get()
	return buttonSelected


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = layers_number.get()
	return userInput


# this is a function to get the selected list box value
def getListboxValue():
	itemSelected = loss_function.curselection()
	return itemSelected


# this is a function to get the selected list box value
def getListboxValue():
	itemSelected = optimizer.curselection()
	return itemSelected


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = epochs_number.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = batch_number.get()
	return userInput


# this is the function called when the button is clicked
def start_function():
	print('clicked')



root = Tk()
#this is the declaration of the variable associated with the radio button group
Yes = tk.StringVar()



# This is the section of code which creates the main window
root.geometry('724x431')
root.configure(background='#FFFFFF')
root.title('Deep Learning Solver')


# This is the section of code which creates a button
Button(root, text='Open', bg='#FFFFFF', font=('arial', 12, 'normal'), command=open_file).place(x=22, y=31)


# This is the section of code which creates the a label
Label(root, text='Filename', bg='#FFFFFF', font=('arial', 12, 'normal')).place(x=92, y=41)


# This is the section of code which creates a button
Button(root, text='Manual', bg='#FFFFFF', font=('arial', 12, 'normal'), command=manual_mode).place(x=502, y=41)


# This is the section of code which creates a button
Button(root, text='Auto', bg='#FFFFFF', font=('arial', 12, 'normal'), command=auto_mode).place(x=612, y=41)


# This is the section of code which creates the a label
Label(root, text='Scale Data', bg='#FFFFFF', font=('arial', 12, 'normal')).place(x=22, y=121)


# This is the section of code which creates a group of radio buttons
frame=Frame(root, width=0, height=0, bg='#FFFFFF')
frame.place(x=112, y=101)
ARBEES=[
('Yes', 'InVisible visibleValue'), 
('No', 'InvisibleValue'), 
]
for text, mode in ARBEES:
	scale=Radiobutton(frame, text=text, variable=Yes, value=mode, bg='#FFFFFF', font=('arial', 12, 'normal')).pack(side='top', anchor = 'w')


# This is the section of code which creates the a label
Label(root, text='Number of Layers:', bg='#FFFFFF', font=('arial', 12, 'normal')).place(x=352, y=121)


# This is the section of code which creates a text input box
layers_number=Entry(root)
layers_number.place(x=492, y=121)


# This is the section of code which creates a listbox
loss_function=Listbox(root, bg='#FFFFFF', font=('arial', 12, 'normal'), width=0, height=0)
loss_function.insert('0', 'MSE')
loss_function.insert('1', 'MSLE')
loss_function.insert('2', 'MAE')
loss_function.insert('3', 'BC')
loss_function.insert('4', 'Hinge')
loss_function.insert('5', 'SHinge')
loss_function.insert('6', 'CC')
loss_function.insert('7', 'S-CC')
loss_function.insert('8', 'KLD')
loss_function.place(x=92, y=231)


# This is the section of code which creates a listbox
optimizer=Listbox(root, bg='#FFFFFF', font=('arial', 12, 'normal'), width=0, height=0)
optimizer.insert('0', 'SGD')
optimizer.insert('1', 'Adam')
optimizer.place(x=172, y=371)


# This is the section of code which creates the a label
Label(root, text='Epochs', bg='#FFFFFF', font=('arial', 12, 'normal')).place(x=242, y=361)


# This is the section of code which creates the a label
Label(root, text='Batch Size', bg='#FFFFFF', font=('arial', 12, 'normal')).place(x=242, y=391)


# This is the section of code which creates a text input box
epochs_number=Entry(root)
epochs_number.place(x=332, y=361)


# This is the section of code which creates a text input box
batch_number=Entry(root)
batch_number.place(x=332, y=391)


# This is the section of code which creates a button
Button(root, text='Start', bg='#FFFFFF', font=('arial', 15, 'bold'), command=start_function).place(x=582, y=371)


root.mainloop()
