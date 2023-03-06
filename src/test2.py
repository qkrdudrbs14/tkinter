import tkinter

#default setting
win = tkinter.Tk() # 대소문자 구분
win.geometry("600x400+100+100")
win.resizable(0,0)

#Label
label1=tkinter.Label(win, text="Hello") # 위젯이름=tkinter.Label(윈도우창, text="내용")을 사용하여 윈도우 창에 Label 위젯을 설정
label1.pack()    # 위젯이름.pack()을 사용하여 위젯을 배치

label2=tkinter.Label(win, text="python", width=10, height=5, fg="red", relief="solid")
label2.pack()

label3=tkinter.Label(win, text="0", width=10, height=5, fg="blue", relief="solid")
label3.pack()

#Button
count = 0
def countUp():
    global count    # local에서 할당이 이루어져 오류가 나므로 global로 선언하여 global 변수라는 것을 알려줘함
    count += 1
    label3.config(text=str(count))

button1 = tkinter.Button(win, overrelief="solid", width=15, command=countUp, repeatdelay=100, repeatinterval=100)
button1.pack()

win.mainloop()