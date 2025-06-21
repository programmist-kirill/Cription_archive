import os
import sys

sys.path.append("/home/kirill/Cription_archive/For_linux/Manager_password/")
#импорт модуля для записи буквы или имени флешки и для проверки пароля на этой флешке
import write_and_check_usb


def count_start_log(user_name):
    """
    подсчет количество запусков программы
    """

    #проверка на существование файла count_start.log
    if os.path.exists("/home/" + user_name + "/Cription_archive/For_linux/count_start.log"):
        
        #чтение файла count_start.log
        with open("/home/" + user_name + "/Cription_archive/For_linux/count_start.log","r") as file:
            count_start = file.read()
        
        #преобразование строки в число
        count_start = int(count_start)
        
        #увеличение числа на единицу
        count_start += 1

        #преобразование числа в строку
        count_start = str(count_start)

        #запись строки в файл
        with open("/home/" + user_name + "/Cription_archive/For_linux/count_start.log","w") as fp:
            fp.write(count_start)

        #запуск модуля для записи буквы или имени флешки и для проверки пароля на этой флешке
        write_and_check_usb.check(user_name)

    else:
        #если нет файла count_start.log
        count_start = "1"
        
        #он записывает в файл единицу 
        with open("/home/" + user_name + "/Cription_archive/For_linux/count_start.log","w") as fp:
            fp.write(count_start)
        
        #запуск модуля для записи буквы или имени флешки и для проверки пароля на этой флешке
        write_and_check_usb.write(user_name)