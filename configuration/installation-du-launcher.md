# 📥 Installation du Launcher

Pour l'instant, le launcher ne s'installe pas directement et a besoin de prérequis. Cette page a été réalisé dans le but de pouvoir vous montrer comment installer le launcher.

{% hint style="warning" %}
Si vous avez besoin d'aide, n'hésitez pas à rejoindre le serveur Discord afin de faire parvenir votre problème ou vos questions.
{% endhint %}

## Installation du Launcher

Télécharger le launcher avec le lien ci dessous. Une fois ceci fait ouvrez le.

{% hint style="danger" %}
Vous devez installer Python et les librairies requises avant d'installer le launcher !
{% endhint %}

### Librairies

{% hint style="warning" %}
Les librairies ne peuvent être installés uniquement après l'installation de Python.
{% endhint %}

{% tabs %}
{% tab title="Plyer" %}
### Librairie Plyer

Elle permet au launcher d'envoyer des notifications sur votre ordinateur.



```powershell
pip install plyer
```
{% endtab %}

{% tab title="Minecraft lib" %}
### Librairie Minecraft Lib

Permet au launcher d'accéder au fichiers de minecraft, de vous télécharger la dernière version et de vérifier vos identifiants.&#x20;

```
pip install minecraft-launcher-lib
```
{% endtab %}

{% tab title="PyPresence" %}
### PyPresence

Permet de gérer et d'activer la Rich Presence sur Discord.

```
pip install pypresence
```
{% endtab %}
{% endtabs %}

Les autres librairies utilisés dans le projet ne nécessite pas d'une installation.

### Télécharger les fichiers du launcher

#### Depuis l'invite de commande Windows

```batch
curl https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe -o python.exe
```

#### Depuis Github

{% embed url="https://github.com/Luckyluka17/CubeCraft-Launcher/releases" %}

## Bonus : Installation de la police d'écriture (recommandé)

Télécharger ce [fichier](https://raw.githubusercontent.com/Luckyluka17/CubeCraft-Launcher/main/Fichiers/Autres/font.ttf). Ensuite, ouvrez le et cliquez sur installer (pas imprimer)

![](<../.gitbook/assets/image (6).png>)
