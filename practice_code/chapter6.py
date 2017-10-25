import tkinter as tk  # imports
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import *
import os
import tkinter.filedialog
import tools_tips as tt
from threading import Thread
import time
from time import sleep
from queue import Queue
import New_queue as bq
from tkinter import filedialog as fd
from os import path
from os import makedirs
from socketserver import BaseRequestHandler, TCPServer
import URL as url



class RequestHandler(BaseRequestHandler):
    # override base class handle method
    def handle(self):
        print('Server connected to: ', self.client_address)
        while True:
            rsp = self.request.recv(512)
            if not rsp: break
            self.request.send(b'Server received: ' + rsp)

# help(TCPServer)
def startServer():
    serv = TCPServer(('', 24000), RequestHandler)

    serv.serve_forever()


# Module level GLOBALS
GLOBAL_CONST = 42
fDir = path.dirname(__file__)
netDir = fDir + '/Backup'
if not path.exists(netDir):
    makedirs(netDir, exist_ok=True)


class OOP():
    def useQueues(self):
        guiQueue = Queue()
        print(guiQueue)
        for idx in range(10):
            guiQueue.put('Message from a queue: ' + str(idx))
        while True:
            print(guiQueue.get())

    def __init__(self):
        # Create instance
        self.win = tk.Tk()
        # Add a title
        self.win.title("Python GUI")
        self.createWidgets()
        self.guiQueue = Queue()
        self.defaultFileEntries()
        # Start TCP/IP server in its own thread
        #self.svrT = Thread(target=startServer, daemon=True)
        #self.svrT.start()

    def defaultFileEntries(self):
        self.fileEntry.delete(0, tk.END)

        self.fileEntry.insert(0, fDir)
        if len(fDir) > self.entryLen:
            self.fileEntry.config(width=len(fDir) + 3)
            self.fileEntry.config(state='readonly')
        self.netwEntry.delete(0, tk.END)
        self.netwEntry.insert(0, netDir)
        if len(netDir) > self.entryLen:
            self.netwEntry.config(width=len(netDir) + 3)

    # help(Spinbox.bind)
    def clickme(self):
        self.action.configure(text='Hello ' + self.name.get() + ' ' + 'you are' + ' ' +
                                   self.age.get() + 'years old')
        print(self)
        bq.writeToScrol(self)
        # self.createThread()
        # for idx in range(3):
        # time.sleep(5)
        # self.scr.insert(tk.INSERT, str(idx) + '\n')
        sleep(2)
        htmlData = url.getHtml()
        print(htmlData)
        self.scr.insert(tk.INSERT, htmlData)


    def radCall(self):  # 6
        radSel = self.radVar.get()
        if radSel == 1:
            self.monty.configure(text=COLOR1)
        elif radSel == 2:
            self.monty.configure(text=COLOR2)
        elif radSel == 3:
            self.monty.configure(text=COLOR3)
            # Spinbox callback

    def _spin(self):
        value = self.spin.get()
        global strData
        strData = self.spin.get()
        print("Spinbox value: " + strData)
        print(value)
        self.scr.insert(tk.INSERT, value + '\n')

    def radCal1(self):
        radSel = self.radVar2.get()
        if radSel == 0:
            self.win.configure(background=colors[0])
        elif radSel == 1:
            self.win.configure(background=colors[1])
        elif radSel == 2:
            self.win.configure(background=colors[2])

    def methodInAThread(self, numOfLoops=10):
        print('Hi, how are you?')
        for idx in range(numOfLoops):
            time.sleep(1)
            self.scr.insert(tk.INSERT, str(idx) + '\n')
            time.sleep(1)
            print('methodInAThread():', self.runT.isAlive())

    def createThread(self, arg):
        self.runT = Thread(target=self.methodInAThread, args=[9])
        self.runT.setDaemon(True)
        self.runT.start()
        print(self.runT)
        print('createThread():', self.runT.isAlive())

        # textBoxes are the Consumers of Queue data
        writeT = Thread(target=self.useQueues, daemon=True)
        writeT.start()

    # Create Queue instance
    # Button Callback
    def getFileName(self):
        print('hello from getFileName')
        # fDir = path.dirname(__file__)
        fName = fd.askopenfilename(parent=self.win, initialdir=fDir)
        print(fName)
        self.fileEntry.delete(0, tk.END)
        self.fileEntry.insert(0, fName)

    def _quit(self):  # 7
        self.win.quit()
        self.win.destroy()
        exit()
        # Display a Message Box
        # Callback function

    def _msgBox(self):
        mBox.showinfo('Python Message Info Box', 'A Python GUI createdusing tkinter:\nThe year is 2017.')
        mBox.showwarning('Python Message Warning Box',
                         'A Python GUI created using tkinter:\nWarning: There might be a bug in this code.')
        mBox.showerror('Python Message Error Box',
                       'A Python GUI createdusing tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
        answer = mBox.askyesno('Python Message Dual Choice Box', 'Are you sure need todo this?')
        print(answer)

    def _openpicture(self):
        default_dir = r"C:\Users"  # 设置默认打开目录
        fname = tk.filedialog.askopenfilename(title=u"选择文件",
                                              initialdir=(os.path.expanduser(default_dir)))
        print(fname)  # 返回文件全路径
        # print (tk.filedialog.askdirectory() ) # 返回目录路径

    # win = tk.Tk()  # Create instance
    # win.title("Python GUI")  # Add a title
    # win.resizable(0,0)

    # Change the main windows icon
    # win.iconbitmap(r'C:\Python\DLLs\pyc.ico')
    def createWidgets(self):
        tabControl = ttk.Notebook(self.win)  # Create Tab Control

        tab1 = ttk.Frame(tabControl)  # Create a tab
        tabControl.add(tab1, text='Tab 1')  # Add the tab

        tab2 = ttk.Frame(tabControl)  # Add a second tab
        tabControl.add(tab2, text='Tab 2')

        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text='Tab 3')

        tab3 = tk.Frame(tab3, bg='blue')
        tab3.pack()
        for orangeColor in range(4):
            canvas = tk.Canvas(tab3, width=150, height=80, highlightthickness=0, bg='orange')
            canvas.grid(row=orangeColor, column=orangeColor)

        tabControl.pack(expand=1, fill="both")  # Pack to make visible
        tabControl.select(1)

        self.monty = ttk.LabelFrame(tab1, text=' Monty Python ')
        self.monty.grid(column=0, row=0, padx=8, pady=4)

        self.monty2 = ttk.LabelFrame(tab2, text=' The Snake ')
        self.monty2.grid(column=0, row=0, padx=8, pady=4)

        self.aLabel = ttk.Label(self.monty, text="Enter your name")
        self.aLabel.grid(column=0, row=0, sticky='W')

        self.name = tk.StringVar()
        self.nameEntered = ttk.Entry(self.monty, width=24, textvariable=self.name)
        self.nameEntered.grid(column=0, row=1, sticky='W')
        self.nameEntered.focus()
        self.nameEntered.delete(0, tk.END)
        self.nameEntered.insert(0, '< default name >')

        ttk.Label(self.monty, text='your age').grid(column=1, row=0)

        self.age = tk.StringVar()
        self.agechosen = ttk.Combobox(self.monty, width=14, textvariable=self.age, state='readonly')
        self.agechosen['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
        self.agechosen.grid(column=1, row=1)
        self.agechosen.current(0)

        self.action = ttk.Button(self.monty, text='click me', command=self.clickme)
        self.action.grid(column=2, row=1)

        self.chVarDis = tk.IntVar()  # 2
        self.check1 = tk.Checkbutton(self.monty2, text="Disabled", variable=self.chVarDis, state
        ='disabled')  # 3
        self.check1.select()
        self.check1.grid(column=0, row=4, sticky=tk.W)  # 5

        self.chVarUn = tk.IntVar()  # 6
        self.check2 = tk.Checkbutton(self.monty2, text="UnChecked", variable=self.chVarUn)
        self.check2.deselect()  # 8
        self.check2.grid(column=1, row=4, sticky=tk.W)  # 9
        self.chVarEn = tk.IntVar()  # 10
        self.check3 = tk.Checkbutton(self.monty2, text="Enabled", variable=self.chVarEn)
        self.check3.select()  # 12
        self.check3.grid(column=2, row=4, sticky=tk.W, columnspan=3)  # 13

        # Radiobutton Globals # 1
        global COLOR1, COLOR2, COLOR3

        COLOR1 = "Blue"  # 2
        COLOR2 = "Gold"  # 3
        COLOR3 = "Red"  # 4

        # Radiobutton Callback # 5

        # create three Radiobuttons # 7
        self.radVar = tk.IntVar()  # 8
        # radVar = tk.IntVar()
        self.rad1 = tk.Radiobutton(self.monty, text=COLOR1, variable=self.radVar, value=1, command=self.radCall)  # 9
        self.rad1.grid(column=0, row=5, sticky=tk.W)  # 10
        self.rad2 = tk.Radiobutton(self.monty, text=COLOR2, variable=self.radVar, value=2, command=self.radCall)  # 11
        self.rad2.grid(column=1, row=5, sticky=tk.W)  # 12
        self.rad3 = tk.Radiobutton(self.monty, text=COLOR3, variable=self.radVar, value=3, command=self.radCall)  # 13
        self.rad3.grid(column=2, row=5, sticky=tk.W)  # 14

        # Adding a Spinbox widget
        # spin = Spinbox(monty, from_=0, to=100,width=5,bd=5,command=_spin)
        self.spin = Spinbox(self.monty, value=(1, 2, 40, 64, 80, 128), width=5, relief=tk.GROOVE, bd=5,
                            command=self._spin)
        self.spin.grid(column=0, row=2, sticky='W')

        tt.createToolTip(self.spin, 'This is a Spin control.')

        scrolW = 40
        scrolH = 10
        self.scr = scrolledtext.ScrolledText(self.monty, width=scrolW, height=scrolH, wrap=tk.WORD)
        self.scr.grid(column=0, sticky='WE', columnspan=3)

        # Add a Tooltip to the ScrolledText widget
        tt.createToolTip(self.scr, 'This is a ScrolledText widget.')
        global colors
        colors = ["Blue", "Gold", "Red"]
        self.radVar2 = tk.IntVar()
        self.radVar2.set(99)

        for col in range(3):  # 3
            curRad = 'rad' + str(col)
            self.curRad = tk.Radiobutton(self.monty2, text=colors[col], variable=self.radVar2, value=col,
                                         command=self.radCal1)
            self.curRad.grid(column=col, row=7, sticky=tk.W)

        self.labelsFrame2 = ttk.LabelFrame(self.monty2, text=' Labels in a Frame2 ')
        self.labelsFrame2.grid(column=0, row=8, padx=20, pady=20)

        self.labelsFrame = ttk.LabelFrame(self.labelsFrame2, text=' Labels in a Frame  ')  # 1
        self.labelsFrame.grid(column=0, row=0)

        ttk.Label(self.labelsFrame, text="Label1").grid(column=0, row=0)
        ttk.Label(self.labelsFrame, text="Label2").grid(column=1, row=1)
        ttk.Label(self.labelsFrame, text="Label3").grid(column=2, row=2)

        for child in self.labelsFrame.winfo_children():
            child.grid_configure(padx=4, pady=4)

        self.menuBar = Menu(self.win)
        self.win.config(menu=self.menuBar)

        self.fileMenu = Menu(self.menuBar)
        self.fileMenu.add_command(label="New")
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self._quit)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        # Add another Menu to the Menu Bar and an item
        # Create Manage Files Frame
        mngFilesFrame = ttk.LabelFrame(tab2, text=' Manage Files: ')
        mngFilesFrame.grid(column=0, row=1, sticky='WE', padx=10, pady=5)

        # Add Widgets to Manage Files Frame
        lb = ttk.Button(mngFilesFrame, text="Browse to File...",
                        command=self.getFileName)
        lb.grid(column=0, row=0, sticky=tk.W)

        self.file = tk.StringVar()
        self.entryLen = scrolW
        self.fileEntry = ttk.Entry(mngFilesFrame, width=self.entryLen,
                                   textvariable=self.file)
        self.fileEntry.grid(column=1, row=0, sticky=tk.W)

        self.logDir = tk.StringVar()
        self.netwEntry = ttk.Entry(mngFilesFrame, width=self.entryLen,
                                   textvariable=self.logDir)
        self.netwEntry.grid(column=1, row=1, sticky=tk.W)

        def copyFile():
            import shutil

            src = self.fileEntry.get()  # fName not use ,well it cause error
            file = src.split('/')[-1]
            dst = self.netwEntry.get() + '/' + file
            try:
                shutil.copy(src, dst)
                mBox.showinfo('Copy File to Network',
                              'Success: File copied.')

            except FileNotFoundError as err:
                mBox.showerror('Copy File to Network',
                               '*** Failed to copy file! ***\n\n' + str(err))
            except Exception as ex:
                mBox.showerror('Copy File to Network',
                               '*** Failed to copy file! ***\n\n' + str(ex))

        cb = ttk.Button(mngFilesFrame, text="Copy File To : ",
                        command=copyFile)
        cb.grid(column=0, row=1, sticky=tk.E)
        # Add some space around each label
        for child in mngFilesFrame.winfo_children():
            child.grid_configure(padx=6, pady=6)

        self.helpmenu = Menu(self.menuBar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self._msgBox)
        self.menuBar.add_cascade(label='help', menu=self.helpmenu)

        self.spicture = ttk.Button(self.monty, text='Select a picture', command=self._openpicture)
        self.spicture.grid(column=1, row=9)

        # booldata=check3.getboolean('s')

        # print(booldata)

        # win.mainloop()  # Start GUI


oop = OOP()

oop.win.mainloop()
