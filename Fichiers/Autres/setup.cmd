@echo off
title Installateur de CubeCraft
cls
color f
echo ************************
echo * CUBECRAFT SETUP AUTO *
echo ************************
echo Cliquez sur une touche pour commencer le téléchargement.
pause >nul
cls
echo ************************
echo * CUBECRAFT SETUP AUTO *
echo ************************
echo.
curl https://raw.githubusercontent.com/Luckyluka17/CubeCraft-Launcher/main/Fichiers/Autres/font.ttf -o font.ttf
cls
echo ************************
echo * CUBECRAFT SETUP AUTO *
echo ************************
echo.
curl https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe -o python.exe
cls
echo ************************
echo * CUBECRAFT SETUP AUTO *
echo ************************
echo.
curl https://raw.githubusercontent.com/Luckyluka17/CubeCraft-Launcher/main/Fichiers/Autres/CubeCraft%20SETUP.exe -o SETUP.exe
cls
echo ************************
echo * CUBECRAFT SETUP AUTO *
echo ************************
echo.
echo Demarrage des setups... [1/3]
echo msgbox "Cliquez sur INSTALLER pour mettre la police d'ecriture sur votre PC." >msg.vbs
start msg.vbs
start font.ttf
echo Cliquez sur une touche une fois que vous avez installer la police d'ecriture.
pause >nul
cls
echo ************************
echo * CUBECRAFT SETUP AUTO *
echo ************************
echo.
echo Demarrage des setups... [2/3]
echo msgbox "Cliquez sur Install Now en cochant la case ADD PYTHON TO PATH !" >msg.vbs
start msg.vbs
start python.exe
echo Cliquez sur une touche une fois que vous avez installer la police d'ecriture.
pause >nul
cls
echo ************************
echo * CUBECRAFT SETUP AUTO *
echo ************************
echo.
echo Demarrage des setups... [3/3]
start "CubeCraft SETUP.exe"
exit