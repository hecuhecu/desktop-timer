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
#timeLabel = Label(root, textvariable=time)

start_stop_button = StringVar()
start_stop_button.set("START")

start = True
stop = True
check = False

def start():
    global input_sec,input_min,start,stop,check,value_time
    start = False
    if stop == True and check == True:
        start = True
        start_stop_button.set("STOP")
        timer()
    elif stop == False and check == True:
        # count_sec = int(text_sec.get())
        # count_min = int(text_min.get())
        # text_sec.set("0")
        # text_min.set("0")
        text_sec.set(int(text_sec.get()))
        text_min.set(int(text_min.get()))
        check = True
        start_stop_button.set("START")
    else:
        start = True
        stop = True
        start_stop_button.set("STOP")
        text_sec.set(int(text_sec.get()))
        text_min.set(int(text_min.get()))
        maximum_time = int(text_min.get())*60+int(text_sec.get())
        #print(maximum_time)
        value_time = 0
        div_time = 1
        #progressbar.configure(maximum=maximum_time,value=value_time)
        timer()
    
def timer():
    global start,text_sec,text_min,check,value_time,div_time
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
                value_time += 1
                #progressbar.configure(value=value_time)
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
    check = True
    stop = False
    time_sec = 0
    time_min = 0
    text_sec.set(str(time_sec))
    text_min.set(str(time_min))

labbel=Label(root,text="設定")
labbel.grid(row=0,column=0,columnspan=1)
    
entry=Entry(root,width=2,font=my_font,textvariable=input_min)
entry.grid(row=0,column=1)

label_min=Label(root,text=u"分")
label_min.grid(row=0,column=2)

entry1=Entry(root,width=2,font=my_font,textvariable=input_sec)
entry1.grid(row=0,column=3)

label_sec=Label(root,text=u"秒")
label_sec.grid(row=0,column=4)

button=Button(root,textvariable=start_stop_button,command=start)
button.grid(row=0,column=5)

button=Button(root,text=u"RESET",command=stop)
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





# #ラベルの配置
# #timeLabel.pack()

# #ボタンの作成
# startButton = Button(root, text="開始")
# stopButton = Button(root, text="一時停止")
# cancelButton = Button(root, text="キャンセル")

# #ボタンの配置
# startButton.pack()
# stopButton.pack()
# cancelButton.pack()

root.mainloop()