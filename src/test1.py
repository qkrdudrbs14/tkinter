# basic 1
import os
import tkinter

win = tkinter.Tk()
win.title('PYG')    #제목
win.geometry("640x400+100+100") #너비x높이+x좌표+y좌표
win.resizable(False, False) #.resizeable(상하, 좌우) 창크기 조절가능 여부 , True=1, False=0을 의미하여 상수를 입력해도 적용이 가능
win.mainloop()