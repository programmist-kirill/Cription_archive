import os
import sys

sys.path.append("Manager_password/")
#импорт модуля который будет хешировать пароль
import hash_password


def main(directory_to_archive , directory_data , password_archive):
    """
    эта функция нужна чтобы сначало вызвать модуля хеширования , потом прочитать пароль , инициализировать переменную с командой для архивации данных и переменной с директорией где должен находится скрипт , затем запустить Си скрипт для записи в файл(я так сделал из за того что у меня на python-не не создавался файл скрипта(commande.sh)) 
    """

    hash_password.main(password=password_archive)

    with open("C:/Cription_archive/For windows/password.sha","r") as file:
        password = file.read()

    commande = "7z.exe a -tzip -ssw -mx1 -p" + password + " -r0 " + directory_to_archive + " " + directory_data

    with open("C:/Cription_archive/For windows/commande.bat" ,"w") as fp:
        fp.write(commande)
    
    os.startfile("C:/Cription_archive/For windows/commande.bat")
    os.remove("C:/Cription_archive/For windows/commande.bat")