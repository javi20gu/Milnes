
import sqlite3


def login(email: str, password: str):

    root = sqlite3.connect("login.db")
    cursor = root.cursor()

    autentificado: bool = False

    cursor.execute("SELECT Email, Password FROM login")
    usuarios = cursor.fetchmany(-1)

    for usuario in usuarios:
        if usuario[0] == email and usuario[1] == password:
            print("---------Has Iniciado Sesión---------")
            autentificado = True
            cursor.execute("SELECT Email, Password, Usuario FROM login WHERE Email='{}'".format(usuario[0]))
            e = cursor.fetchone()
            root.commit()
            root.close()
            return True, e

    if not autentificado:
        print("---------Intentelo de Nuevo: Email o Contraseña Incorrecta---------")
        return [False]

    root.commit()
    root.close()
