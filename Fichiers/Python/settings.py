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
    lch1 = chck1.get()
    fichier3 = open("check1.ini", "w")
    fichier3.write(str(lch1))
    fichier3.close()
    fichier4 = open("check2.ini", "w")
    lch2 = chck2.get()
    fichier4.write(str(lch2))
    fichier4.close()
    lch3 = chck3.get()
    fichier5 = open("check3.ini", "w")
    fichier5.write(str(lch3))
    fichier5.close()
    a1.close()
    a2.close()
    a3.close()
    a4.close()
    a5.close()
    os.system('exit')
    window1.destroy()

window1 = Tk()
window1.title("Settings")
window1.geometry("300x425")
window1.resizable(width=False, height=False)
window1.iconbitmap('icon2.ico')

chck1 = IntVar()
chck2 = IntVar()
chck3 = IntVar()

Label(window1, text="Paramètres", font=("Lobster", 25)).pack()
Label(window1, text="Connexion", font=("Comic sans MS", 17)).pack()
Label(window1, text="Adresse-mail", font=("Comic sans MS", 15)).pack()
username = Entry(window1, width=30)
username.pack()
Label(window1, text="Mot de passe", font=("Comic sans MS", 15)).pack()
mdp = Entry(window1, width=30, show="•")
mdp.pack()
Button(window1, text="Appliquer", font=("Comic sans MS", 12), command=apply).place(x=120, y=370)
Label(text="Identifiants de votre compte Microsoft", font=("Comic sans MS", 9)).pack()
check1 = Checkbutton(text="Sauvegarder les identifiants", font=("Comic sans MS", 12), variable=chck1, onvalue=1, offvalue=0)
check1.pack()
Label(window1, text="Minecraft", font=("Comic sans MS", 17)).pack()
check2 = Checkbutton(text="Jouer sur la dernière version", font=("Comic sans MS", 12), variable=chck2, onvalue=1, offvalue=0)
check2.pack()
check3 = Checkbutton(text="Activer Download Booster (beta)", font=("Comic sans MS", 12), variable=chck3, onvalue=1, offvalue=0)
check3.pack()

a1 = open("password.ini","r")
a2 = open("pseudo.ini","r")
a3 = open("check1.ini","r")
a4 = open("check2.ini","r")
a5 = open("check3.ini","r")

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