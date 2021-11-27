import minecraft_launcher_lib
import subprocess
import sys
import os

e_mail = open("pseudo.ini","r")
motdepasse = open("password.ini","r")

def launch(email, mdp):
    latest_version = minecraft_launcher_lib.utils.get_latest_version()["release"]

    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

    minecraft_launcher_lib.install.install_minecraft_version(latest_version, minecraft_directory)

    login_data = minecraft_launcher_lib.microsoft_account.complete_login(email, mdp)

    options = {
        "username": login_data["name"],
        "uuid": login_data["id"],
        "token": login_data["access_token"]
    }
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(latest_version, minecraft_directory, options)

    subprocess.call(minecraft_command)

try:
    launch(e_mail, motdepasse)
except:
    print("Une erreur est survenue lors du démarrage de minecraft.")
    os.system("pause")
    exit()