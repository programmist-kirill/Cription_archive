#этот скрипт нужен для инициализацйии(получении необходимой информации) и компилирования скрипта для записи скрипта(commande.sh)

import os
import getpass

#импрорт модуля для подсчета количества запуска программы
import count_start

#модуль main нужен чтобы получить информацию от пользователя и запустить create_archive.py или unzipping_archive.py 
import main

#этот модуль нужен чтобы установить 7zip на все семейства дистрибутивов(debian , fedora и arch linux)
import installing_7zip


def what_user_name():
    """
    эта функция нужна чтобы если нет файла с именем пользователя он ее записал , и чтобы при надобности установить 7zip , и всегда запускать модули count_start и main
    """


    #получение имя пользователя
    user_name = getpass.getuser()

    #если нет count_start.log , тобишь при первом запуске , и запись имя пользователя в файл

    directory_C_script = "/home/" + user_name + "/Cription_archive/For_linux/file_writer.c"
    directory_to_compilations = "/home/" + user_name + "/Cription_archive/For_linux/file_writer"
    #компиляция file_writer.c , который создает файл скрипта для архивации и разархивации
    os.system("gcc " + directory_C_script + "-o " + directory_to_compilations)
    
    if not os.path.exists("/home/" + user_name + "/Cription_archive/For_linux/count_start.log"):
        with open("/home/" + user_name + "/Cription_archive/For_linux/user_name","w") as fp:
            fp.write(user_name)
        
        #запуск модуля установки 7zip
        installing_7zip()

    #запуст модуля count_start с параметром "имя_пользователя"
    count_start.count_start_log(user_name)
    
    #запуск модуля main с параметром "имя_пользователя"
    main.main(user_name)

#вызов функции
what_user_name()
