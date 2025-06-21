#Этот модуль нужен для разархивации архива

import os
import sys


sys.path.append("/home/kirill/Cription_arc0hive/For_linux/Manager_password/")
#импорт модуля хеширования пароля
import hash_password

def main(directory_to_archive , directory_to_unzipping , password_archive , user_name):
    """
    В этой функции сначало хешируется пароль , потом читается файл с паролем , и запускает скрипт для создания файла
    """
    hash_password.main(user_name , password=password_archive)

    with open("/home/" + user_name + "/Cription_archive/For_linux/password.sha","r") as file:
        password = file.read()

    directory = "/home/" + user_name + "/Cription_archive/For_linux/commande.sh"
    commande = "#!/bin/bash\n7z x " + directory_to_archive +  " -p" + password +  " -o" + directory_to_unzipping + " -y"

    os.system(f"./file_writer {directory} {commande}") 