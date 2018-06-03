from pathlib import Path
from subprocess import call
from sys import exit
from Crear_Sesión import crear_sesion
from Iniciar_Sesión import login


def main():

    base_de_datos = Path("login.db")

    if not base_de_datos.exists():
        print("\U0001f504", "Configurando todo...")
        call("python run_datebase.py")

    menu = True
    initial = False

    while menu:
        print("\n=============== Bienvenido a Milnes ===============")

        if initial:
            print("\nBienvenido:", datos[1][-1], "\n")

        print("\nSeleccione la opción que desea: \n 1] Iniciar Sesión\n 2] Crear Sesión\n 3] Salir")
        opcion = int(input(">>>"))

        if opcion == 1:
            email = input("Introduce tu Email: ")
            password = input("Introduce tu Password: ")

            datos = login(email, password)
            initial = datos[0]

        elif opcion == 2:
            usuario = input("Introduce tu nuevo Usuario: ")
            apellidos = input("Introduce tus nuevos Apellidos:")
            edad = int(input("Introduce tu Edad: "))
            email = input("Introduce tu nuevo Email: ")
            password = input("Introduce tu nuevo Password: ")

            crear_sesion(usuario, apellidos, edad, email, password)

        elif opcion == 3:
            break
            exit()


if __name__ == '__main__':
    main()
