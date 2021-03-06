from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

#メインウィンドウ作成
root = Tk()

#ウィンドウタイトルとサイズを設定
root.title("タイマー")
root.geometry("500x100")
root.attributes("-topmost", True)

#入力
input_sec = StringVar()
input_min = StringVar()
input_sec.set("0")
input_min.set("1")
my_font=font.Font(size=20)

#時間の表示
text_sec = StringVar()
text_min = StringVar()
text_sec.set("0")
text_min.set("0")

start_stop_button = StringVar()
start_stop_button.set("開始")

#動いていない（スタートが無効,ストップが有効）
start = False
stop = True
initial_startup = True

def tap_start_stop():
    global input_sec,input_min,start,stop,initial_startup

    if start == False and stop == True and initial_startup == False:
        start = True
        stop = False
        start_stop_button.set("一時停止")
        button1["state"] = DISABLED
        timer()
    elif start == True and stop == False and initial_startup == False:
        start = False
        stop = True
        start_stop_button.set("開始")
        button1["state"] = NORMAL
        timer()
    else:
        start = True
        stop = False
        initial_startup = False
        start_stop_button.set("一時停止")
        text_sec.set(int(input_sec.get()))
        text_min.set(int(input_min.get()))
        timer()

def timer():
    global start,text_sec,text_min
    if start == True:
        if int(text_sec.get()) == 0 and int(text_min.get()) == 0:
            pass
        else:
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
                start_stop_button.set("開始")
                messagebox.showwarning("終了", "時間になりました")
                time_min = 0
                time_sec = 0
                text_sec.set(str(time_sec))
                text_min.set(str(time_min))

def stop():
    global start,stop,initial_startup
    start = False
    stop = True
    initial_startup = True
    button1["state"] = DISABLED
    time_sec = 0
    time_min = 0
    text_sec.set(str(time_sec))
    text_min.set(str(time_min))

def slider_scroll(self):
    window_transparency = 1 - val.get()/100
    root.attributes("-alpha",window_transparency)

labbel = ttk.Label(root,text="設定")
labbel.grid(row=0,column=0,columnspan=1)
    
entry = ttk.Entry(root,width=2,font=my_font,textvariable=input_min)
entry.grid(row=0,column=1)

label_min = ttk.Label(root,text="分")
label_min.grid(row=0,column=2)

entry1 = ttk.Entry(root,width=2,font=my_font,textvariable=input_sec)
entry1.grid(row=0,column=3)

label_sec = ttk.Label(root,text="秒")
label_sec.grid(row=0,column=4)

button = ttk.Button(root,textvariable=start_stop_button,command=tap_start_stop)
button.grid(row=0,column=5)

button1 = ttk.Button(root,text="リセット",state=DISABLED,command=stop)
button1.grid(row=0,column=6)

labbel = ttk.Label(root,text="タイマー")
labbel.grid(row=1,column=0,columnspan=1)

labbel = ttk.Label(root,font=my_font,textvariable=text_min)
labbel.grid(row=1,column=1,columnspan=1)

labbel = ttk.Label(root,text="分")
labbel.grid(row=1,column=2,columnspan=1)

labbel = ttk.Label(root,font=my_font,textvariable=text_sec)
labbel.grid(row=1,column=3,columnspan=1)

labbel = ttk.Label(root,text="秒")
labbel.grid(row=1,column=4,columnspan=1)

val = DoubleVar()
scale = ttk.Scale(root,variable=val,from_=0,to=100,command=slider_scroll)
scale.grid(row=1,column=5
)

label = ttk.Label(root, text="透明度")
label.grid(row=1,column=6)

root.mainloop()