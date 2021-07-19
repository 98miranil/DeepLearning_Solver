#GUI APP

import tkinter as tk
from tkinter import *

def load_layers():
    num_layers = int(float(ent_layers.get()))
    for i in range(num_layers):
        print(i)
    

window = tk.Tk()
window.title("Deep Learning Solver")

content = tk.Frame(window)
#window.columnconfigure([0,1,2,3], weight = 1, minsize = 50)
'''
for i in range (5):
    window.columnconfigure(i, weight = 1, minsize = 100)
window.rowconfigure([0,1,2], weight = 1, minsize = 200)
'''

'''
Upper part -- Settings Frame with widgets
'''
fr_settings = tk.Frame(content, relief = tk.RAISED)
btn_open = tk.Button(fr_settings, text = "Open", padx = 5, pady = 5)
lbl_filename = tk.Label(fr_settings, text = "Filename")
lbl_space = tk.Label(fr_settings, text = " ")
#btn_manual = tk.Button(fr_settings, text = "Manual", padx = 5, pady = 5)
btn_auto = tk.Button(fr_settings, text = "Auto", padx = 5, pady = 5)

#Listbox Scale Data
lbl_scale = tk.Label(fr_settings, text = "Scale Data", pady = 40 )
lb_scale = Listbox(fr_settings, bg = 'white', fg = 'black', selectbackground = 'green', selectmode = 'SINGLE', height = 2, width = 7)
lb_scale.insert('0', 'Yes')
lb_scale.insert('1', 'No')

lbl_layers = tk.Label(fr_settings, text = "Layers")
ent_layers = tk.Entry(fr_settings, width=10)
btn_model = tk.Button(fr_settings, text = "Model", padx = 5, pady = 5, command = load_layers)

#Model
fr_model = tk.Frame(content, relief = tk.RAISED)

lbl_nodes = tk.Label(fr_model, text = "Nodes") #Falta fer el grid

'''
Grid of the Settings widgets
'''
content.grid(column=0, row = 0)
btn_open.grid(row = 0, column = 0, padx = 15, pady = 5)
lbl_filename.grid(row = 0, column = 1)
lbl_space.grid(row = 0, column = 2, padx = 150)
#btn_manual.grid(row = 0, column = 3, padx = 5)
btn_auto.grid(row = 0, column = 3)
fr_settings.grid(row = 0, column = 0, sticky = "n")

lbl_scale.grid(row = 1, column = 0)
lb_scale.grid(row = 1, column = 1)
lbl_layers.grid(row = 1, column = 2, sticky = "e")
ent_layers.grid(row = 1, column = 3)
btn_model.grid(row = 1, column = 4, padx = 20)
window.mainloop()