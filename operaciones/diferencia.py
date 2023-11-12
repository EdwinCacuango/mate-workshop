from utilidades import listar_conjuntos
# Funcion que lista opciones en diferencias
def mostrar_opciones():
    print("¿Qué tipo de interacción buscas realizar?")
    print("1. A - B")
    print("2. B - A")

    preference = input("Opción seleccionada: ")
    return int(preference)

#Funcion de diferencia simple
def diferencia(conjuntoA, conjuntoB):
    print("3.Diferencia entre conjuntos\n")
    
    listar_conjuntos(conjuntoA, conjuntoB)

    #Seleccionar orden de intersección
    user_preference = mostrar_opciones()

    if user_preference == 1 :
        conjuntoD1 = conjuntoA - conjuntoB
        print(f"A - B = {conjuntoD1}")
        print("N(A-B) = ",len(conjuntoD1))
        print()
    elif user_preference == 2 :
        conjuntoD2 = conjuntoB - conjuntoA
        print(f"B - A = {conjuntoD2}")
        print("N(B-A) = ",len(conjuntoD2))
        print()
    else :
        print("Opcion incorrecta\n")
        user_preference = mostrar_opciones()


#Funcion de diferencia simetrica
def diferencia_simetrica(conjuntoA, conjuntoB):
    print("4.Diferencia Simétrica\n")
    
    listar_conjuntos(conjuntoA, conjuntoB)

    conjuntoDS = conjuntoA ^ conjuntoB

    print(f"A Δ B = {conjuntoDS}")
    print("N(A Δ B) = ",len(conjuntoDS))
    print()