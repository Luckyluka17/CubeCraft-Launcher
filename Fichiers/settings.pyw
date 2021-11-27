from tkinter import *
import os


def apply():
    pseudo = username.get()
    fichier1 = open("pseudo.ini","w")
    fichier1.write(pseudo)
    fichier1.close()
    password = mdp.get()
    fichier2 = open("password.ini", "w")
    fichier2.write(password)
    fichier2.close()
    a1.close()
    a2.close()
    os.system('exit')
    window1.destroy()

window1 = Tk()
window1.title("Settings")
window1.geometry("300x400")
window1.resizable(width=False, height=False)
window1.iconbitmap('icon.ico')

Label(window1, text="Paramètres", font=("Lobster", 25)).pack()
Label(window1, text="Compte Mojang", font=("Comic sans MS", 17)).pack()
Label(window1, text="Pseudo", font=("Comic sans MS", 15)).pack()
username = Entry(window1, width=30)
username.pack()
Label(window1, text="Mot de passe", font=("Comic sans MS", 15)).pack()
mdp = Entry(window1, width=30, show="•")
mdp.pack()
Button(window1, text="Appliquer", font=("Comic sans MS", 12), command=apply).place(x=120, y=350)

a1 = open("password.ini","r")
a2 = open("pseudo.ini","r")

mdp.insert(0,a1.read())
username.insert(0,a2.read())

window1.mainloop()