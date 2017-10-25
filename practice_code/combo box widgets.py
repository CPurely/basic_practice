import tkinter as tk # 1
from tkinter import ttk
from tkinter import scrolledtext




win = tk.Tk()
win.title("Python GUI")
#win.resizable(0,0)
#ttk.Label(win,text='label').grid(column=2,row=2)
aLabel = ttk.Label(win, text="Enter your name")
aLabel.grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()


ttk.Label(win,text='your age').grid(column=1,row=0)

age=tk.StringVar()
agechosen=ttk.Combobox(win,width=12,textvariable=age,state='readonly')
agechosen['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
agechosen.grid(column=1,row=1)
agechosen.current(0)

def clickme():
    action.configure(text='Hello ' + name.get() + ' ' +'you are'+' '+
                          age.get()+'years old')

action=ttk.Button(win,text='click me',command=clickme)
action.grid(column=2,row=1)

chVarDis = tk.IntVar() # 2
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state
='disabled') # 3
check1.select()
check1.grid(column=0, row=4, sticky=tk.W) # 5

chVarUn = tk.IntVar() # 6
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect() # 8
check2.grid(column=1, row=4, sticky=tk.W) # 9
chVarEn = tk.IntVar() # 10
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select() # 12
check3.grid(column=2, row=4, sticky=tk.W) # 13


# Radiobutton Globals # 1
COLOR1 = "Blue" # 2
COLOR2 = "Gold" # 3
COLOR3 = "Red" # 4
# Radiobutton Callback # 5
def radCall(): # 6
    radSel=radVar.get()
    if radSel == 1: win.configure(background=COLOR1)
    elif radSel == 2: win.configure(background=COLOR2)
    elif radSel == 3: win.configure(background=COLOR3)
# create three Radiobuttons # 7
radVar = tk.IntVar() # 8
radVar1 = tk.IntVar()
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar1, value=1,command=radCall) # 9
rad1.grid(column=0, row=5, sticky=tk.W) # 10
rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall) # 11
rad2.grid(column=1, row=5, sticky=tk.W) # 12
rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall) # 13
rad3.grid(column=2, row=5, sticky=tk.W) # 14

scrolW=30
scrolH=5
scr=scrolledtext.ScrolledText(win,width=scrolW,height=scrolH,wrap=tk.CHAR)
scr.grid(column=0,columnspan=3)

colors = ["Blue", "Gold", "Red"]
radVar2 = tk.IntVar()
radVar2.set(99)

def radCal1():
    radSel=radVar2.get()
    if radSel == 0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])


for col in range(3): # 3
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(win, text=colors[col],variable=radVar2, value=col, command=radCal1)
    curRad.grid(column=col, row=7, sticky=tk.W)



win.mainloop()
