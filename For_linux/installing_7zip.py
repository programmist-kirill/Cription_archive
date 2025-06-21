import os
import sys

#этот модуль нужен для установки 7zip на все семейства дистрибутивов linux

def arch():
    """
    установка 7zip в archlinux с помощью pacman
    """
    os.system("sudo pacman -S 7zip")

def debian():
    """
    установка 7zip в debian с помощью apt
    """
    os.system("sudo apt install p7zip-full")

def fedora():
    """
    установка 7zip в fedora с помощью dnf
    """
    os.system("sudo dnf install p7zip p7zip-plugins")

def main():
    """
    функция спрашивает к какому семейству относится их дистрибутив
    """
    print("0 - arch linux")
    print("1 - debian")
    print("2 - fedora")

    system_family = input("Какое семейство у вашего дистрибутива - ")
    if system_family == "0":
        arch()
    
    elif system_family == "1":
        debian()
    
    elif system_family == "2":
        fedora()
    
    else:
        print("Введите коректнную информацию")
        sys.exit()