from os import system
system("cls")
bienvenida = str("\t **Bienvenido : Programa que resuelve operaciones entre conjuntos**\n")
print(bienvenida)
conjuntoA = set(input("Ingrese los elementos del conjunto A separados por espacios:\n ").split())

system("cls")
print(bienvenida)

conjuntoB = set(input("Ingrese los elementos del conjunto B separados por espacios:\n ").split())


system("cls")
print(bienvenida)
print(f"Su conjunto A es: {conjuntoA} \nSu conjunto B es: {conjuntoB}\n")
print("\t\t .:MENU:.\n")
print("1.Union entre conjuntos")
print("2.Interseccion entre conjuntos")
print("3.Diferencia entre conjuntos")
print("4.Diferencia Simétrica")
print("5.Comprobar si es un subconjunto")
print("6.Anadir - Editar - Eliminar elementos de un conjunto\n")

opcion = int(input("Elija una opción: "))

if opcion == 1 :
    system("cls")
    print(bienvenida)
    print()
    print("1.Union entre conjuntos:\n")
    print(f"Su conjunto A es: {conjuntoA} \nSu conjunto B es: {conjuntoB}\n")
    conjuntoU = conjuntoA | conjuntoB
    print(f"A ∪ B = {conjuntoU}")
    print("N(A ∪ B) = ",len(conjuntoU))
    print()
elif opcion == 2 :
    system("cls")
    print(bienvenida)
    print("2.Interseccion entre conjuntos:\n")
    print(f"Su conjunto A es: {conjuntoA} \nSu conjunto B es: {conjuntoB}\n")
    conjuntoI = conjuntoA & conjuntoB
    print(f"A ∩ B = {conjuntoI}")
    print("N(A ∩ B) = ",len(conjuntoI))
    print()
elif opcion == 3 :
    system("cls")
    print(bienvenida)
    print("3.Diferencia entre conjuntos\n")
    print(f"Su conjunto A es: {conjuntoA} \nSu conjunto B es: {conjuntoB}\n")
    opcion1 = int(input("Desea realizar :\n1. A - B\n2. B - A\n\n"))
    if opcion1 == 1 :
        conjuntoD1 = conjuntoA - conjuntoB
        print(f"A - B = {conjuntoD1}")
        print("N(A-B) = ",len(conjuntoD1))
        print()
    elif opcion1 == 2 :
        conjuntoD2 = conjuntoB - conjuntoA
        print(f"B - A = {conjuntoD2}")
        print("N(B-A) = ",len(conjuntoD2))
        print()
    else :
        print("Opcion incorrecta\n")

elif opcion == 4 :
    system("cls")
    print(bienvenida)
    print("4.Diferencia Simétrica\n")
    print(f"Su conjunto A es: {conjuntoA} \nSu conjunto B es: {conjuntoB}\n")
    conjuntoDS = conjuntoA ^ conjuntoB
    print(f"A Δ B = {conjuntoDS}")
    print("N(A Δ B) = ",len(conjuntoDS))
    print()

elif opcion == 5 :
    system("cls")
    print(bienvenida)
    print("5.Comprobar si es un subconjunto\n")
    if conjuntoA.issubset(conjuntoB) :
        print("A es subconjunto de B")
    elif conjuntoB.issubset(conjuntoA) :
        print("B es subconjunto de A")
    else :
        print("No existen subconjuntos")
