from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('My clock')


def time():
    current_time = strftime('%H:%M:%S %p')
    lbl.config(text=current_time)
    lbl.after(1000, time)


lbl = Label(root, font=('helvetica', 40), background='tan1', foreground='gray25')
notation = Label(root, text="    Hours       Minutes       Seconds",
                 font=('helvetica', 10), background='tan1', foreground='gray25')
lbl.pack(anchor='center')
notation.pack(side='left', expand='True', fill='both')
time()

root.mainloop()