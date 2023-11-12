from utilidades import saludar_y_limpiar
from operaciones.union import *
from operaciones.interseccion import *
from operaciones.diferencia import diferencia, diferencia_simetrica
from operaciones.subconjunto import subconjunto

saludar_y_limpiar()
conjuntoA = set(input("Ingrese los elementos del conjunto A separados por espacios:\n ").split())
conjuntoB = set(input("Ingrese los elementos del conjunto B separados por espacios:\n ").split())


saludar_y_limpiar()
listar_conjuntos(conjuntoA, conjuntoB)

print("\t\t .:MENU:.\n")
print("1.Union entre conjuntos")
print("2.Interseccion entre conjuntos")
print("3.Diferencia entre conjuntos")
print("4.Diferencia Simétrica")
print("5.Comprobar si es un subconjunto")
print("6.Anadir - Editar - Eliminar elementos de un conjunto\n")

opcion = int(input("Elija una opción: "))

if opcion == 1 :
    saludar_y_limpiar()
    union(conjuntoA, conjuntoB)
elif opcion == 2 :
    saludar_y_limpiar()
    interseccion(conjuntoA, conjuntoB)
elif opcion == 3 :
    saludar_y_limpiar()
    diferencia(conjuntoA, conjuntoB)
elif opcion == 4 :
    saludar_y_limpiar()
    diferencia_simetrica(conjuntoA, conjuntoB)
elif opcion == 5 :
    saludar_y_limpiar()
    subconjunto(conjuntoA, conjuntoB)

