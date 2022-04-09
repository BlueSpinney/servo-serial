from tkinter import *
import pyautogui
import serial
import time


mousepos = []
empty = ""
main = Tk()
oldx = 0
oldy = 0
con = 0
counter = 0
con = 0

arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1)


def stop():
    global con,counter
    if counter == 0:
        con = 1
        counter = 0
        b2.pack_forget()
        xl.pack_forget()
        yl.pack_forget()
        b1.pack()
        counter = 1
    elif counter == 1:
        con=0
        counter = 0
    if con == 1:
        xl.after(1000,stop)


def collect_mouse():
    global empty,mousepos,oldx,oldy,con,counter
    b1.pack_forget()
    b2.pack()
    xl.pack()
    yl.pack()
    mousepos = pyautogui.position()
    x = mousepos.x
    y = mousepos.y
    x = x / 1919
    y = y / 1079
    x = x * 180
    y = y * 180
    x = int(x)
    y = int(y)
    print(x)
    print(y)
    if oldx != x or oldy != y:
        xl.configure(text="x : " + str(x))
        yl.configure(text="y : " + str(y))
        arduino.write(bytes(str(x),'utf-8'))
        time.sleep(0.05)
        arduino.write(bytes(str(y),'utf-8'))
        time.sleep(0.05)
        ret = arduino.readline()
        print(ret)

    oldx = x
    oldy = y
    if con == 0:
        b1.after(50,collect_mouse)




b1 = Button(main,text="start",command=collect_mouse)
b2 = Button(main,text="stop",command=stop)
xl = Label(main,text="")
yl = Label(main,text="")


b1.pack()
main.mainloop()
