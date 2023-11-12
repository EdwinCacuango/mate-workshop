import os

mensaje_bienvenida = "**Bienvenido : Programa que resuelve operaciones entre conjuntos**\n"

# Esta funcion valida el tipo de sistema y cambia el comando para limpiar el terminal
def limpieza_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def saludar_y_limpiar ():
    limpieza_terminal()
    print(mensaje_bienvenida)

def listar_conjuntos(conjuntoA, conjuntoB):
    print(f"Su conjunto A es: {conjuntoA}\n")
    print(f"Su conjunto B es: {conjuntoB}\n")