import tkinter
from math import *

win = tkinter.Tk()
win.title("PYG")
win.geometry("640x480+100+100")
win.resizable(0,0)

#entry
def calc(event):
    label.config(text="결과="+str(eval(entry.get())))

entry = tkinter.Entry(win)
entry.bind("<Return>", calc)
entry.pack()

label = tkinter.Label(win)
label.pack()

win.mainloop()