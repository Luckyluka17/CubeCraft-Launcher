from tkinter import *
import os
import webbrowser
import time

os.system('pip install pypresence')

from pypresence import Presence
ID = '913877663544918067'
try:
    RPC = Presence(ID)
    RPC.connect()
    RPC.update(
        state="Dev par Luckyluka17",
        details="CubeCraft v1.0",
        large_image="image",
        large_text="CubeCraft Launcher"
    )
except:
    print("Discord n'est pas ouvert")


def settings():
    os.system("start settings.pyw")

def site():
    webbrowser.open("https://sites.google.com/view/luckyluka17/projets/projets-actuels/cubecraft-launcher")

def mc_launch():
    os.system("start main.py")


window = Tk()
window.title("CubeCraft Client")
bg = PhotoImage(file="background.png")
background = Label(window, image=bg)
background.place(x=0, y=0, relwidth=1, relheight=1)
icone = PhotoImage(file="icon.png")
window.geometry("480x480")
window.resizable(width=False, height=False)
window.iconbitmap('icon.ico')


title =  Label(text="                                        CubeCraft Launcher Client                                        ", font=("Lobster", 13)).pack()
bouton1 = Button(text="Jouer à Minecraft", font=("Comic Sans MS", 15), bg='green', command=mc_launch)
bouton1.place(x=148, y=400)
bouton2 = Button(text="⚙️", font=("Comic Sans MS", 10), command=settings)
bouton2.place(x=0, y=0)
bouton2 = Button(text="🌍", font=("Comic Sans MS", 10), command=site)
bouton2.place(x=30, y=0)
text1 = Label(text="Développé par Luckyluka 17", font=("Comic Sans MS", 10)).pack()

window.mainloop()