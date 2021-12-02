from tkinter import *
import time

window = Tk()

window.overrideredirect(True)

def center_window(width=300, height=200):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

def loading():
    os.system('start launcher.pyw')
    window.destroy()


center_window(512, 512)
import os
bg = PhotoImage(file="launcher.png")
background = Label(window, image=bg)
background.place(x=0, y=0, relwidth=1, relheight=1)
window.update()
time.sleep(1)
loading()