from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# --------------------------------------------------------------
fig = Figure(figsize=(12, 8), facecolor='white')
# --------------------------------------------------------------
# axis = fig.add_subplot(111) # 1 row, 1 column, only graph
axis = fig.add_subplot(311)  # 2 rows, 1 column, Top graph
# --------------------------------------------------------------
xValues = [1, 2, 3, 4]
yValues = [5, 7, 6, 8]
axis.plot(xValues, yValues,label='1')
axis.set_xlabel('Horizontal Label')
axis.set_ylabel('Vertical Label')
# axis.grid() # default line style
axis.grid(linestyle='-')  # solid grid lines
axis1 = fig.add_subplot(312) # 2 rows, 1 column, Bottom graph
#--------------------------------------------------------------
xValues1 = [1,2,3,4]
yValues1 = [7,5,8,6]
axis1.plot(xValues1, yValues1,label='2')
axis1.grid()

axis.legend(loc=2)
axis1.legend(loc=0)
#fig.tight_layout()
# --------------------------------------------------------------
def _destroyWindow():
    root.quit()
    root.destroy()


# --------------------------------------------------------------
root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)
# --------------------------------------------------------------
canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
# --------------------------------------------------------------
root.update()
root.deiconify()
root.mainloop()
