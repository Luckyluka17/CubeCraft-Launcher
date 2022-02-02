from tkinter import *
import os
import webbrowser
import time
from plyer import notification
from tkinter.messagebox import showinfo

window2 = Tk()

window2.overrideredirect(True)

def center_window2(width=300, height=200):
    # get screen width and height
    screen_width = window2.winfo_screenwidth()
    screen_height = window2.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window2.geometry('%dx%d+%d+%d' % (width, height, x, y))

def loading():
    def site():
        webbrowser.open("https://sites.google.com/view/luckyluka17/projets/projets-actuels/cubecraft-launcher")


    def mc_launch():
        os.system("start main.exe")

    def settings():

        window.destroy()
        
        def apply():
            with open("password.ini","w") as f:
                f.write(mdp.get())
                f.close()

            with open("pseudo.ini","w") as f:
                f.write(username.get())
                f.close()
                
            os.system("start launcher.py")
            window1.destroy()

        window1 = Tk()
        window1.title("Settings")
        window1.geometry("300x425")
        window1.resizable(width=False, height=False)
        window1.iconbitmap('icon2.ico')

        chck1 = IntVar()
        chck2 = IntVar()
        chck3 = IntVar()

        a1 = open("password.ini","r")
        a2 = open("pseudo.ini","r")
        a3 = open("check1.ini","r")
        a4 = open("check2.ini","r")
        a5 = open("check3.ini","r")

        def btncheck1():
            with open("check1.ini","w") as f:
                f.write(str(chck1.get()))
                print(str(chck1.get()))
                f.close()

        def btncheck2():
            with open("check2.ini","w") as f:
                f.write(str(chck2.get()))
                print(str(chck2.get()))
                f.close()

        def btncheck3():
            with open("check3.ini","w") as f:
                f.write(str(chck3.get()))
                print(str(chck3.get()))
                f.close()


        Label(window1, text="Paramètres", font=("Lobster", 25)).pack()
        Label(window1, text="Connexion", font=("Comic sans MS", 17)).pack()
        Label(window1, text="Adresse-mail", font=("Comic sans MS", 15)).pack()
        username = Entry(window1, width=30)
        username.pack()
        Label(window1, text="Mot de passe", font=("Comic sans MS", 15)).pack()
        mdp = Entry(window1, width=30, show="•")
        mdp.pack()
        Button(window1, text="Appliquer", font=("Comic sans MS", 12), command=apply).place(x=120, y=370)
        Label(window1, text="Identifiants de votre compte Microsoft", font=("Comic sans MS", 9)).pack()
        check1 = Checkbutton(window1, text="Sauvegarder les identifiants", font=("Comic sans MS", 12), variable=chck1, onvalue=1, offvalue=0, command=btncheck1)
        check1.pack()
        Label(window1, text="Minecraft", font=("Comic sans MS", 17)).pack()
        check2 = Checkbutton(window1, text="Jouer sur la dernière version", font=("Comic sans MS", 12), variable=chck2, onvalue=1, offvalue=0, command=btncheck2)
        check2.pack()
        check3 = Checkbutton(window1, text="Activer RPC Discord", font=("Comic sans MS", 12), variable=chck3, onvalue=1, offvalue=0, command=btncheck3)
        check3.pack()

        mdp.insert(0,a1.read())
        username.insert(0,a2.read())

        if a3.read() == "0":
            check1.deselect()
        else:
            check1.select()

        if a4.read() == "0":
            check2.deselect()
        else:
            check2.select()

        if a5.read() == "0":
            check3.deselect()
        else:
            check3.select()
        
        
        window1.mainloop()

    window2.destroy()
        
    window = Tk()

    a55 = open("check3.ini","r")

    if a55.read() == "1":
        print("RPC activé")
        from pypresence import Presence
        ID = '913877663544918067'
        try:
            RPC = Presence(ID)
            RPC.connect()
            RPC.update(
                state="Dev par Luckyluka17",
                details="CubeCraft v.1.0.2",
                large_image="image",
                large_text="CubeCraft Launcher"
            )
            notification.notify(
            title = "CubeCraft Launcher",
            message = "Rich Presence Discord activé !",
            app_icon = "icon3.ico",
            timeout = 5,
            )
        except:
            print("Discord n'est pas ouvert")
    else:
        print("RPC désactivé")

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


center_window2(512, 512)
bg = PhotoImage(file="launcher.png")
background = Label(window2, image=bg)
background.place(x=0, y=0, relwidth=1, relheight=1)
window2.update()
time.sleep(1)
loading()