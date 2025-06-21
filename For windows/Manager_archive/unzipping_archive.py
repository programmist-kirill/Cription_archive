#Этот модуль нужен для разархивации архива

import os
import sys

sys.path.append("Manager_password/")
#импорт модуля хеширования пароля
import hash_password

def main(directory_to_archive , directory_to_unzipping , password_archive):
    """
    В этой функции сначало хешируется пароль , потом читается файл с паролем , и запускает скрипт для создания файла
    """
    hash_password.main(password=password_archive)

    with open("C:/Cription_archive/For windows/password.sha","r") as file:
        password = file.read()

    commande = "7z.exe x " + directory_to_archive +  " -p" + password +  " -o" + directory_to_unzipping + " -y"

    with open("C:/Cription_archive/For windows/commande.bat" ,"w") as fp:
        fp.write(commande)
    
    os.startfile("C:/Cription_archive/For windows/commande.bat")
    os.remove("C:/Cription_archive/For windows/commande.bat")