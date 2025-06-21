import os
import sys

sys.path.append("/home/kirill/Cription_archive/For_linux/Manager_archive/")
#импорт модуля для разархивации архива
import unzipping_archive

#импорт модуля для архивации данных в архив
import create_archive


def main(user_name):
    print("\n\n1 - открыть архив")
    print("2 - создать архив")

    action = input("Что вы хотите сделать: ")
    if action == "1":
        directory_to_archive = input("Где находится архив - ")
        #проверка архива на существование
        if os.path.exists(directory_to_archive):
            print('')       
        
        else:
            #если архив не найден , скрипт выводит сообщение как выйти из программы
            print("Архив не найден")
            input("Для продолжения нажмите Enter")
            sys.exit()

        directory_to_unzipping = input("Куда распаковывать архив - ")
        password_to_archive = input("Введите пароль от архива - ")

        #запуск модуля разархивирования архива , с параметрами - имя пользователя , директория где находится архив , директория куда распаковывать архив , пароль от архива
        unzipping_archive.main(user_name , directory_to_archive , directory_to_unzipping , password_archive=password_to_archive)

    
    elif action == "2":
        directory_to_archive = input("Куда сохранять архив - ")
        directory_data = input("Где находятся данные для архивирования - ")
        #проверка существования данных для архивации
        if os.path.exists(directory_data):
            print("")

        else:
            #если данные не найдены , скрипт выводит сообщение как выйти из программы
            print("Не удается найти папку")
            input("Для продолжения нажмите Enter")
            sys.exit()

        password_to_archive = input("Введите пароль для архива - ")

        #запуск модуля для создания архива , с параметрами - имя пользователя , директория куда сохранять архив , директорию откуда взять данные , пароль для архива
        create_archive.main(user_name ,  directory_to_archive , directory_data , password_archive=password_to_archive)

    else:
        #если пользователь ввел другие данные
        print("Неверный выбор")
        input("Для продолжения нажмите Enter")
        sys.exit()

    #удаления файла содержащего ключ от архива
    os.remove("/home/" + user_name + "/Cription_archive/For_linux/password.sha")