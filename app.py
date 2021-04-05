#GUI APP

import tkinter as tk

window = tk.Tk()
window.title("Deep Learning Solver")
#window.columnconfigure([0,1,2,3], weight = 1, minsize = 50)
for i in range (5):
    window.columnconfigure(i, weight = 1, minsize = 100)
window.rowconfigure([0,1,2], weight = 1, minsize = 200)

'''
Upper part -- Settings Frame with widgets
'''
fr_settings = tk.Frame(window, relief = tk.RAISED)
btn_open = tk.Button(fr_settings, text = "Open", padx = 5, pady = 5)
lbl_filename = tk.Label(fr_settings, text = "Filename")
lbl_space = tk.Label(fr_settings, text = " ")
btn_manual = tk.Button(fr_settings, text = "Manual", padx = 5, pady = 5)
btn_auto = tk.Button(fr_settings, text = "Auto", padx = 5, pady = 5)

'''
Grid of the Settings widgets
'''
btn_open.grid(row = 0, column = 0, padx = 15, pady = 5)
lbl_filename.grid(row = 0, column = 1)
lbl_space.grid(row = 0, column = 2, padx = 300)
btn_manual.grid(row = 0, column = 3, padx = 5)
btn_auto.grid(row = 0, column = 4)
fr_settings.grid(row = 0, column = 0, sticky = "n")
window.mainloop()