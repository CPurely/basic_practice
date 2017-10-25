import tkinter as tk  # imports
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import *
import os
import tkinter.filedialog
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
from numpy.fft import fftfreq
from scipy.fftpack import *
from numpy import *
import PIL  # 导入pillow后matploylib可以支持bmp图像（各种图像格式都支持）
from scipy import misc
import skimage
from skimage import data, exposure, img_as_float, transform

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler

# ------------------------------------------------------------------------------------------------------

h = 0.532e-3
k = 2 * pi / h
i = (-1) ** 0.5


def rgb2gray(rgb):
    return dot(rgb[..., :3], [0.299, 0.587, 0.114])  # define rgb2gray function


def _openpicture():  # 打开图片并转换为灰度图
    default_dir = r"C:\Users"  # 设置默认打开目录
    global fname, img, u1, M, N
    # fname=None                                      #初始化变量，以免下次调用函数，局部变量冲突。也不用，因为python动态性很强，下次调用函数fname会被重新赋值
    fname = tk.filedialog.askopenfilename(title=u"选择文件",
                                          initialdir=(os.path.expanduser(default_dir)))

    img = mpimg.imread(fname)
    lum = img[:, :, 0:3]  # extract rgb data
    # plt.imshow(lum)

    gray = rgb2gray(lum)
    u0 = gray
    M0, N0 = u0.shape
    N = 512
    r = N / N0
    u1 = misc.imresize(u0, r)  # 对图像进行缩放

    # plt.imshow(gray, cmap = plt.get_cmap('gray'))
    # plt.show()
    # print(gray)
    M, N = u1.shape
    # print(fname)                           # 返回文件全路径
    # print (tk.filedialog.askdirectory() ) # 返回目录路径


def caculate_and_plot():
    Z0 = distance.get()
    L0 = dw.get()
    Imethod = method.get()

    Uf = fft2(u1, (M, N))
    Uf = fftshift(Uf)
    II = abs(Uf) ** 2
    II = double(II)
    Gmax = np.amax(II)
    Gmin = np.amin(II)
    rII = skimage.exposure.rescale_intensity(II, in_range=(Gmin, Gmax))  ##错了,应该计算衍射之后的频谱
    print(Gmax)

    if Imethod == 1:  # 角谱衍射传递函数计算衍射
        caculate_and_plot.f.clf()
        caculate_and_plot.a = caculate_and_plot.f.add_subplot(131)  # 原始物光振幅
        caculate_and_plot.a.imshow(u1, cmap='gray')
        caculate_and_plot.a.set_title('Initial picture')
        caculate_and_plot.a.axis("off")

        caculate_and_plot.a1 = caculate_and_plot.f.add_subplot(132)  # 物光波频谱

        caculate_and_plot.a1.imshow(II, cmap='gray')
        caculate_and_plot.a1.set_title('Frequency spectrum')
        caculate_and_plot.a1.axis('off')

        n = arange(1, N + 1)
        x = h * (-N / L0 / 2 + 1 / L0 * (n - 1))
        y = x
        [yy, xx] = meshgrid(y, x)
        trans = exp(i * k * Z0 * (1 - xx ** 2 - yy ** 2) ** 0.5)

        f2 = Uf * trans
        Uf = ifft2(f2, (N, N))  # 对N * N点的离散函数f2作IFFT计算

        If = abs(Uf) ** 2
        If = double(If)

        caculate_and_plot.a2 = caculate_and_plot.f.add_subplot(133)
        caculate_and_plot.a2.imshow(If, cmap='gray')
        caculate_and_plot.a2.set_title('Diffraction picture')  # 衍射图像
        caculate_and_plot.a2.axis('off')

        canvas.show()

    if Imethod == 2:  # 菲涅耳解析传递函数计算衍射
        caculate_and_plot.f.clf()
        caculate_and_plot.a = caculate_and_plot.f.add_subplot(131)  # 原始物光振幅
        caculate_and_plot.a.imshow(u1, cmap='gray')
        caculate_and_plot.a.set_title('Initial picture')
        caculate_and_plot.a.axis("off")

        caculate_and_plot.a1 = caculate_and_plot.f.add_subplot(132)
        caculate_and_plot.a1.imshow(rII, cmap='gray')
        caculate_and_plot.a1.set_title('Frequency spectrum')
        caculate_and_plot.a1.axis('off')

        n = arange(1, N + 1)
        x = h * (-N / L0 / 2 + 1 / L0 * (n - 1))
        y = x
        [yy, xx] = meshgrid(y, x)
        trans = exp(i * k * Z0 * (1 - (xx ** 2 + yy ** 2) / 2))
        f2 = Uf * trans
        Uf = ifft2(f2, (N, N))  # 对N * N点的离散函数f2作IFFT计算

        If = abs(Uf) ** 2
        If = double(If)

        caculate_and_plot.a2 = caculate_and_plot.f.add_subplot(133)
        caculate_and_plot.a2.imshow(If, cmap='gray')
        caculate_and_plot.a2.set_title('Diffraction picture')  # 衍射图像
        caculate_and_plot.a2.axis('off')

        canvas.show()

    if Imethod == 3:
        caculate_and_plot.f.clf()
        caculate_and_plot.a = caculate_and_plot.f.add_subplot(131)  # 原始物光振幅
        caculate_and_plot.a.imshow(u1, cmap='gray')
        caculate_and_plot.a.set_title('Initial picture')
        caculate_and_plot.a.axis("off")

        caculate_and_plot.a1 = caculate_and_plot.f.add_subplot(132)
        caculate_and_plot.a1.imshow(rII, cmap='gray')
        caculate_and_plot.a1.set_title('Frequency spectrum')
        caculate_and_plot.a1.axis('off')

        n = arange(1, N + 1)
        x = -L0 / 2 + L0 / N * (n - 1)
        y = x
        [yy, xx] = meshgrid(y, x)
        f2 = exp(i * k * Z0) / (i * h * Z0)
        f2 = f2 * exp(i * k / 2 / Z0 * (xx ** 2 + yy ** 2))
        f2 = fft2(f2, (N, N))  # 对N * N点的离散函数f2作FFT计算
        trans = fftshift(f2)  # 将FFT计算结果进行整序
        f2 = Uf * trans
        Uf = fft2(f2, (N, N))  # 对N * N点的离散函数f2作FFT计算
        Uf = fftshift(Uf)  # 将FFT计算结果进行整序

        If = abs(Uf) ** 2
        If = double(If)
        If = skimage.transform.rotate(If, 180, resize=False)  # 将图像旋转180度

        caculate_and_plot.a2 = caculate_and_plot.f.add_subplot(133)
        caculate_and_plot.a2.imshow(If, cmap='gray')
        caculate_and_plot.a2.set_title('Diffraction picture')  # 衍射图像
        caculate_and_plot.a2.axis('off')

        canvas.show()

    if Imethod == 4:
        caculate_and_plot.f.clf()
        caculate_and_plot.a = caculate_and_plot.f.add_subplot(131)  # 原始物光振幅
        caculate_and_plot.a.imshow(u1, cmap='gray')
        caculate_and_plot.a.set_title('Initial picture')
        caculate_and_plot.a.axis("off")

        caculate_and_plot.a1 = caculate_and_plot.f.add_subplot(132)
        caculate_and_plot.a1.imshow(rII, cmap='gray')
        caculate_and_plot.a1.set_title('Frequency spectrum')
        caculate_and_plot.a1.axis('off')

        n = arange(1, N + 1)
        x = -L0 / 2 + L0 / N * (n - 1)
        y = x
        [yy, xx] = meshgrid(y, x)
        f2 = exp(i * k * sqrt(Z0 ** 2 + xx ** 2 + yy ** 2))
        f2 = f2 / (i * 2 * h * (Z0 ** 2 + xx ** 2 + yy ** 2))
        f2 = f2 * ((Z0 ** 2 + xx ** 2 + yy ** 2) ** 0.5 + Z0)
        f2 = fft2(f2, (N, N))  # 对N * N点的离散函数f2作FFT计算
        trans = fftshift(f2)  # 将FFT计算结果进行整序
        f2 = Uf * trans
        Uf = fft2(f2, (N, N))  # 对N * N点的离散函数f2作FFT计算
        Uf = fftshift(Uf)  # 将FFT计算结果进行整序
        # Uf = imrotate(Uf, 180)

        If = abs(Uf) ** 2
        If = double(If)
        If = skimage.transform.rotate(If, 180, resize=False)  # 将图像旋转180度

        caculate_and_plot.a2 = caculate_and_plot.f.add_subplot(133)
        caculate_and_plot.a2.imshow(If, cmap='gray')
        caculate_and_plot.a2.set_title('Diffraction picture')  # 衍射图像
        caculate_and_plot.a2.axis('off')

        canvas.show()

    if Imethod == 5:
        caculate_and_plot.f.clf()
        caculate_and_plot.a = caculate_and_plot.f.add_subplot(131)  # 原始物光振幅
        caculate_and_plot.a.imshow(u1, cmap='gray')
        caculate_and_plot.a.set_title('Initial picture')
        caculate_and_plot.a.axis("off")

        caculate_and_plot.a1 = caculate_and_plot.f.add_subplot(132)
        caculate_and_plot.a1.imshow(rII, cmap='gray')
        caculate_and_plot.a1.set_title('Frequency spectrum')
        caculate_and_plot.a1.axis('off')

        n = arange(1, N + 1)
        x = -L0 / 2 + L0 / N * (n - 1)
        y = x
        [yy, xx] = meshgrid(y, x)
        f2 = exp(i * k * sqrt(Z0 ** 2 + xx ** 2 + yy ** 2))
        f2 = f2 / (i * h * (Z0 ** 2 + xx ** 2 + yy ** 2))
        f2 = fft2(f2, (N, N))  # 对N * N点的离散函数f2作FFT计算
        trans = fftshift(f2)  # 将FFT计算结果进行整序
        f2 = Uf * trans
        Uf = fft2(f2, (N, N))  # 对N * N点的离散函数f2作FFT计算
        Uf = fftshift(Uf)  # 将FFT计算结果进行整序
        # Uf = imrotate(Uf, 180)

        If = abs(Uf) ** 2
        If = double(If)
        If = skimage.transform.rotate(If, 180, resize=False)  # 将图像旋转180度

        caculate_and_plot.a2 = caculate_and_plot.f.add_subplot(133)
        caculate_and_plot.a2.imshow(If, cmap='gray')
        caculate_and_plot.a2.set_title('Diffraction picture')  # 衍射图像
        caculate_and_plot.a2.axis('off')

        canvas.show()

        # fig = plt.figure()
        # ax = fig.add_subplot(111)
        # ax.imshow(u1,cmap="gray")
        # ax.set_title("initial picture")
        # plt.axis("off")

        # Uf = fft2(u1, (M, N))
        # Uf = fftshift(Uf)
        # II = abs(Uf) ** 2
        # II = double(II)
        # Gmax = np.amax(II)
        # Gmin = np.amin(II)

        # rII = skimage.exposure.rescale_intensity(II, in_range=(Gmin, Gmax), out_range='dtype')   ##错了,应该计算衍射之后的频谱

        # fig2 = plt.figure()
        # ax2 = fig2.add_subplot(111)
        # ax2.imshow(rII, cmap='gray')
        # ax2.set_title('frequence domain')

        # plt.show()

        # dw=(h*M*z0)**0.5


if __name__ == '__main__':
    matplotlib.use("TkAgg")

    win = tk.Tk()  # Create instance
    win.title("Python GUI")  # Add a title
    win.resizable(0, 0)

    monty = ttk.LabelFrame(win, text=' DFFT 衍射计算')
    monty.grid(column=1, row=0, padx=8, pady=4)

    # ----------------------------选择需要处理的图片--------------------------------------------------------

    spicture = ttk.Button(monty, text='Select a picture', command=_openpicture)
    spicture.grid(column=0, row=0)

    idd = ttk.Label(monty, text='初始衍射距离=1000(mm)')  # initial diffraction distance
    idd.grid(column=0, row=1)

    dd = ttk.Label(monty, text='输入你想要的衍射距离(mm)')  # diffraction distance
    dd.grid(column=0, row=2)

    distance = tk.DoubleVar()
    distance.set(1000)
    distanceEntry = ttk.Entry(monty, width=12, textvariable=distance)
    distanceEntry.grid(column=1, row=2)
    distanceEntry.focus()

    idw = ttk.Label(monty, text='根据采样定理计算得到的初始场宽度L0=16.5041(mm)')  # initial diffraction width
    idw.grid(column=0, row=3)

    dw = tk.DoubleVar()
    dw.set(16.5041)
    dwEntry = ttk.Entry(monty, width=12, textvariable=dw)
    dwEntry.grid(column=1, row=3)

    mLabel = tk.Label(monty, text='请选择一个方法:\n1:角谱\n2:菲涅尔解析\n3:菲涅尔FFT\n4:基尔霍夫\n5:瑞利索末菲')
    mLabel.grid(column=0, row=4, rowspan=6)

    method = tk.IntVar()
    method.set(1)
    methodChosen = ttk.Combobox(monty, width=10, textvariable=method, state='readonly')
    methodChosen['values'] = (1, 2, 3, 4, 5)
    methodChosen.grid(column=1, row=7)

    upload = ttk.Button(monty, text='Submit your data', command=caculate_and_plot)  # 还是先不要进行任何计算为好，先将用户输入的数据全部获取
    upload.grid(column=0, row=10)
    # print(i)

    caculate_and_plot.f = Figure(figsize=(12, 6), dpi=100)
    canvas = FigureCanvasTkAgg(caculate_and_plot.f, master=monty)
    # caculate_and_plot.canvas.show()
    canvas.get_tk_widget().grid(row=11, columnspan=3)

    testFrame = Frame()
    testFrame.grid(row=12, column=0, columnspan=2)  # 添加图像处理toolbar
    toolbar = NavigationToolbar2TkAgg(canvas, testFrame)
    toolbar.update()

    # caculate_and_plot.canvas._tkcanvas.grid(row=15,column=0)

    def on_key_event(event):
        print('you pressed %s' % event.key)
        key_press_handler(event, canvas, toolbar)


    canvas.mpl_connect('key_press_event', on_key_event)

    # -----------------------------------创建菜单栏---------------------------------------------------------

    def _quit():  # 7
        win.quit()
        win.destroy()
        exit()

    menuBar = Menu(win)
    win.config(menu=menuBar)

    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=_quit)
    menuBar.add_cascade(label="File", menu=fileMenu)


    def _msgBox():
        mBox.showinfo('Python Message Info Box', 'A Python GUI createdusing tkinter:\nThe year is 2017.')
        mBox.showwarning('Python Message Warning Box',
                         'A Python GUI created using tkinter:\nWarning: There might be a bug in this code.')
        mBox.showerror('Python Message Error Box',
                       'A Python GUI createdusing tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
        answer = mBox.askyesno('Python Message Dual Choice Box', 'Are you sure need todo this?')
        print(answer)


    helpmenu = Menu(menuBar, tearoff=0)
    helpmenu.add_command(label="About", command=_msgBox)
    menuBar.add_cascade(label='help', menu=helpmenu)

    # -----------------------------------------------------------------------------------------------------

    win.mainloop()  # Start GUI
