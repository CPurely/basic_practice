import tkinter as tk  # imports
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import *

win = tk.Tk()  # Create instance
win.title("Python GUI")  # Add a title
# win.resizable(0,0)
# Change the main windows icon
win.iconbitmap(r'C:\Python\DLLs\pyc.ico')

tabControl = ttk.Notebook(win)  # Create Tab Control

tab1 = ttk.Frame(tabControl)  # Create a tab
tabControl.add(tab1, text='Tab 1')  # Add the tab

tab2 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab2, text='Tab 2')

tab3=ttk.Frame(tabControl)
tabControl.add(tab3,text='Tab 3')

tab3 = tk.Frame(tab3, bg='blue')
tab3.pack()
for orangeColor in range(2):
    canvas = tk.Canvas(tab3, width=150, height=80,highlightthickness=0, bg='orange')
    canvas.grid(row=orangeColor, column=orangeColor)

tabControl.pack(expand=1, fill="both")  # Pack to make visible

monty = ttk.LabelFrame(tab1, text=' Monty Python ')
monty.grid(column=0, row=0, padx=8, pady=4)

monty2 = ttk.LabelFrame(tab2, text=' The Snake ')
monty2.grid(column=0, row=0, padx=8, pady=4)

aLabel = ttk.Label(monty, text="Enter your name")
aLabel.grid(column=0, row=0, sticky='W')

name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky='W')
nameEntered.focus()

ttk.Label(monty, text='your age').grid(column=1, row=0)

age = tk.StringVar()
agechosen = ttk.Combobox(monty, width=12, textvariable=age, state='readonly')
agechosen['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
agechosen.grid(column=1, row=1)
agechosen.current(0)


def clickme():
    action.configure(text='Hello ' + name.get() + ' ' + 'you are' + ' ' +
                          age.get() + 'years old')


action = ttk.Button(monty, text='click me', command=clickme)
action.grid(column=2, row=1)

chVarDis = tk.IntVar()  # 2
check1 = tk.Checkbutton(monty2, text="Disabled", variable=chVarDis, state
='disabled')  # 3
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)  # 5

chVarUn = tk.IntVar()  # 6
check2 = tk.Checkbutton(monty2, text="UnChecked", variable=chVarUn)
check2.deselect()  # 8
check2.grid(column=1, row=4, sticky=tk.W)  # 9
chVarEn = tk.IntVar()  # 10
check3 = tk.Checkbutton(monty2, text="Enabled", variable=chVarEn)
check3.select()  # 12
check3.grid(column=2, row=4, sticky=tk.W, columnspan=3)  # 13

# Radiobutton Globals # 1
COLOR1 = "Blue"  # 2
COLOR2 = "Gold"  # 3
COLOR3 = "Red"  # 4


# Radiobutton Callback # 5
def radCall():  # 6
    radSel = radVar.get()
    if radSel == 1:
        monty.configure(text=COLOR1)
    elif radSel == 2:
        monty.configure(text=COLOR2)
    elif radSel == 3:
        monty.configure(text=COLOR3)


# create three Radiobuttons # 7
radVar = tk.IntVar()  # 8
# radVar = tk.IntVar()
rad1 = tk.Radiobutton(monty, text=COLOR1, variable=radVar, value=1, command=radCall)  # 9
rad1.grid(column=0, row=5, sticky=tk.W)  # 10
rad2 = tk.Radiobutton(monty, text=COLOR2, variable=radVar, value=2, command=radCall)  # 11
rad2.grid(column=1, row=5, sticky=tk.W)  # 12
rad3 = tk.Radiobutton(monty, text=COLOR3, variable=radVar, value=3, command=radCall)  # 13
rad3.grid(column=2, row=5, sticky=tk.W)  # 14

# Spinbox callback
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

# Adding a Spinbox widget
#spin = Spinbox(monty, from_=0, to=100,width=5,bd=5,command=_spin)
spin = Spinbox(monty, value=(1,2,40,64,80,128),width=5,relief=tk.GROOVE,bd=5,command=_spin)
spin.grid(column=0, row=2,sticky='W')



scrolW = 30
scrolH = 5
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)

colors = ["Blue", "Gold", "Red"]
radVar2 = tk.IntVar()
radVar2.set(99)


def radCal1():
    radSel = radVar2.get()
    if radSel == 0:
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])


for col in range(3):  # 3
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty2, text=colors[col], variable=radVar2, value=col, command=radCal1)
    curRad.grid(column=col, row=7, sticky=tk.W)

labelsFrame2 = ttk.LabelFrame(monty2, text=' Labels in a Frame2 ')
labelsFrame2.grid(column=0, row=8, padx=20, pady=20)

labelsFrame = ttk.LabelFrame(labelsFrame2, text=' Labels in a Frame  ')  # 1
labelsFrame.grid(column=0, row=0)

ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=1, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=2, row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=4, pady=4)


def _quit():  # 7
    win.quit()
    win.destroy()
    exit()


menuBar = Menu(win)
win.config(menu=menuBar)

fileMenu = Menu(menuBar)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)


# Display a Message Box
# Callback function
def _msgBox():
    mBox.showinfo('Python Message Info Box', 'A Python GUI createdusing tkinter:\nThe year is 2017.')
    mBox.showwarning('Python Message Warning Box',
                     'A Python GUI created using tkinter:\nWarning: There might be a bug in this code.')
    mBox.showerror('Python Message Error Box',
                   'A Python GUI createdusing tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
    answer = mBox.askyesno('Python Message Dual Choice Box', 'Are you sure need todo this?')
    print(answer)


# Add another Menu to the Menu Bar and an item


helpmenu = Menu(menuBar, tearoff=0)
helpmenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label='help', menu=helpmenu)

win.mainloop()  # Start GUI
