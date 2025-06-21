import os
import sys

sys.path.append("Manager_password/")
#импорт модуля который нужен для записи названия(буквы) флешки и для проверки ключа на этой флешке
import write_and_check_usb


def count_start_log():
    #если есть файл count_start.log
    if os.path.exists("C:/Cription_archive/For windows/count_start.log"):
        #прочитывание файла
        with open("C:/Cription_archive/For windows/count_start.log","r") as file:
            count_start = file.read()
        
        #преобразование строки в число
        count_start = int(count_start)
        #сложение числа на 1
        count_start += 1
        #преобразование числа в строку
        count_start = str(count_start)

        #запись переменной в файл
        with open("C:/Cription_archive/For windows/count_start.log","w") as fp:
            fp.write(count_start)

        #запуск модуля который проверяет флешку на достоверность
        write_and_check_usb.check()

    else:
        #если файла нет , он записывает в файл единицу
        count_start = "1"
        with open("C:/Cription_archive/For windows/count_start.log","w") as fp:
            fp.write(count_start)
             
        #запуск модуля который записывает в файл букву(название) флешки , и записывает в неё ключ
        write_and_check_usb.write()