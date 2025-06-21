import os
import sys

#импрорт и запуск модуля для подсчета количества запуска программы
import count_start
count_start.count_start_log()

sys.path.append("Manager_archive/")
#импорт модуля для разархивации архива
import unzipping_archive
#импорт модуля для архивации данных в архив
import create_archive


def main():
    print("1 - открыть архив")
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
        password_archive = input("Введите пароль от архива - ")
        
        #запуск модуля разархивирования архива , с параметрами - директория где находится архив , директория куда распаковывать архив , пароль от архива
        unzipping_archive.main(directory_to_archive , directory_to_unzipping , password_archive)

    
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

        password_archive = input("Введите пароль для архива - ")

        #запуск модуля для создания архива , с параметрами - директория куда сохранять архив , директорию откуда взять данные , пароль для архива
        create_archive.main(directory_to_archive , directory_data , password_archive)

    else:
        #если пользователь ввел другие данные
        print("Неверный выбор")
        input("Для продолжения нажмите Enter")
        sys.exit()

    #удаления файла содержащего ключ от архива
    os.remove("C:/Cription_archive/For windows/password.sha")
main()