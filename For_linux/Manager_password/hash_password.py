import hashlib

def main(user_name , password):
    """
    Этот модуль нужен для хеширования пароля методом sha-512
    """
    sha512_hash = hashlib.sha512()
    sha512_hash.update(password.encode('utf-8'))
    hashed_password = sha512_hash.hexdigest()
    
    #запись пароля в файл
    with open("/home/" + user_name + "/Cription_archive/For_linux/password.sha","w") as fp:
        fp.write(hashed_password)