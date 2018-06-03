import sqlite3


def crear_sesion(usuario: str, apellidos: str, edad: int, email: str, password: str):
    conexion = sqlite3.connect("login.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO login (usuario, apellidos, edad, email, password) "
                       "VALUES('{}', '{}','{}','{}','{}')".format(usuario, apellidos,
                                                                  edad, email, password))
        print(f"Su Cuenta ha sido registrada: {email}")
    except sqlite3.IntegrityError:
        print(f"Email ya existente({email})")

    conexion.commit()
    conexion.close()
