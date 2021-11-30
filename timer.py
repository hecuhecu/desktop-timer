from tkinter import *
from tkinter import ttk
from tkinter import font

#メインウィンドウ作成
root = Tk()

#ウィンドウタイトルとサイズを設定
root.title("TIMER")
root.geometry("500x100")

#入力
input_sec = StringVar()
input_min = StringVar()
input_sec.set("0")
input_min.set("30")
my_font=font.Font(size=20)

#時間の表示
text_sec = StringVar()
text_min = StringVar()
text_sec.set("0")
text_min.set("0")

start_stop_button = StringVar()
start_stop_button.set("START")

start = True
stop = False
check = True

def start():
    global input_sec,input_min,start,stop,check
    start = False
    if stop == True and check == True:
        start = True
        start_stop_button.set("STOP")
        timer()
    elif stop == True and check == False:
        text_sec.set(int(text_sec.get()))
        text_min.set(int(text_min.get()))
        check = True
        start_stop_button.set("START")
    else:
        start = True
        stop = True
        start_stop_button.set("STOP")
        text_sec.set(int(input_sec.get()))
        text_min.set(int(input_min.get()))
        timer()
    
def timer():
    global start,text_sec,text_min,check
    if start == True:
        if int(text_sec.get()) == 0 and int(text_min.get()) == 0:
            pass
        else:
            check = False
            time_min = int(text_min.get())
            time_sec = int(text_sec.get())
            if time_min >= 0:
                time_sec -= 1
                text_sec.set(str(time_sec))
                root.after(1000,timer)
                if time_sec == -1:
                    time_min -= 1
                    text_min.set(str(time_min))
                    text_sec.set("59")
            if int(text_sec.get()) == 0 and int(text_min.get()) == 0:
                start = False
                time_min = 0
                time_sec = 0
                text_sec.set(str(time_sec))
                text_min.set(str(time_min))

def stop():
    global start,stop,check
    start = True
    stop = False
    check = True
    time_sec = 0
    time_min = 0
    text_sec.set(str(time_sec))
    text_min.set(str(time_min))

labbel=Label(root,text="設定")
labbel.grid(row=0,column=0,columnspan=1)
    
entry=Entry(root,width=2,font=my_font,textvariable=input_min)
entry.grid(row=0,column=1)

label_min=Label(root,text="分")
label_min.grid(row=0,column=2)

entry1=Entry(root,width=2,font=my_font,textvariable=input_sec)
entry1.grid(row=0,column=3)

label_sec=Label(root,text="秒")
label_sec.grid(row=0,column=4)

button=Button(root,textvariable=start_stop_button,command=start)
button.grid(row=0,column=5)

button=Button(root,text="RESET",command=stop)
button.grid(row=0,column=6)

labbel=Label(root,text="タイマー")
labbel.grid(row=1,column=0,columnspan=1)

labbel=Label(root,font=my_font,textvariable=text_min)
labbel.grid(row=1,column=1,columnspan=1)

labbel=Label(root,text="分")
labbel.grid(row=1,column=2,columnspan=1)

labbel=Label(root,font=my_font,textvariable=text_sec)
labbel.grid(row=1,column=3,columnspan=1)

labbel=Label(root,text="秒")
labbel.grid(row=1,column=4,columnspan=1)

root.mainloop()