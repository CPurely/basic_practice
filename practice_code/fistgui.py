import tkinter as tk # 1
from tkinter import ttk


win = tk.Tk() # 2
win.title("Python GUI") # 3
#win.resizable(0,0)
#ttk.Label(win,text='label').grid(column=2,row=2)
aLabel = ttk.Label(win, text="Enter your name") # 2
aLabel.grid(column=0, row=0)

name = tk.StringVar() # 6
nameEntered = ttk.Entry(win, width=12, textvariable=name) # 7
nameEntered.grid(column=0, row=1)
nameEntered.focus()


def clickMe(): # 5
    action.configure(text='Hello ' + name.get())



action = ttk.Button(win, text="Click Me!", command=clickMe) # 7
action.configure(state='disabled')
action.grid(column=1, row=1)




win.mainloop() # 4
