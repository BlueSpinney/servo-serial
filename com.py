import serial
import time
from tkinter import *

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

main = Tk()

def sendn():
    num = e1.get()
    print("sending : " + str(num))
    arduino.write(bytes(num, 'utf-8'))
    time.sleep(0.05)
    print(arduino.read())


b1 = Button(main,text="send",command=sendn)
e1 = Entry(main,bd=1)


b1.pack()
e1.pack()

main.mainloop()
