import os
from tkinter import ttk
import tkinter as tk 

window = tk.Tk()

def center_window(width=300, height=200):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

window.title("Updater (v1.0.0)")
center_window(300, 55)
window.resizable(False, False)
window.overrideredirect(True)

ttk.Label(
    text=" ",
    font=("Calibri", 5)
).pack()

ttk.Label(
    text="Installation du logiciel en cours...",
    font=("Calibri", 15)
).pack()


window.update()
print("Installation de Python...")
os.system('curl https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe --output "%TMP%\python-3.9.10.exe" && "%TMP%\python-3.9.10.exe" /silent')
print("Installation des modules...")
os.system('pip install plyer')
os.system('pip install minecraft-launcher-lib')
os.system('pip install minecraft-launcher-lib')
os.system('curl https://raw.githubusercontent.com/Luckyluka17/CubeCraft-Launcher/main/Fichiers/Autres/CubeCraft%20SETUP.exe --output "%TMP%\csetup.exe"')
os.system('%TMP%\csetup.exe')
exit()