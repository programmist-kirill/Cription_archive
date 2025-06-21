import os
import getpass
import count_start
import main
import installing_7zip

def what_user_name():
    user_name = getpass.getuser()
    if not os.path.exists("/home/" + user_name + "/Cription_archive/For_linux/count_start.log"):
        with open("/home/" + user_name + "/Cription_archive/For_linux/user_name","w") as fp:
            fp.write(user_name)
        installing_7zip.main()
    
    count_start.count_start_log(user_name)
    main.main(user_name)
what_user_name()