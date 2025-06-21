import os
import sys

sys.path.append("Manager_password/")
#импорт модуля который будет хешировать пароль
import hash_password


def main(user_name , directory_to_archive , directory_data , password_archive):
    """
    эта функция нужна чтобы сначало вызвать модуля хеширования , потом прочитать пароль , инициализировать переменную с командой для архивации данных и переменной с директорией где должен находится скрипт , затем запустить Си скрипт для записи в файл(я так сделал из за того что у меня на python-не не создавался файл скрипта(commande.sh)) 
    """
    hash_password.main(user_name , password=password_archive)

    with open("/home/" + user_name + "/Cription_archive/For_linux/password.sha","r") as file:
        password = file.read()

    commande = "#!/bin/bash\n7z a -tzip -ssw -mx1 -p'" + password + "' -r0 '" + directory_to_archive + "' '" + directory_data + "'"
    directory = "/home/" + user_name + "/Cription_archive/For_linux/commande.sh"

    os.system(f"./file_writer {directory} {commande}") 