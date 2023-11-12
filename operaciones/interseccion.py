from utilidades import listar_conjuntos

def interseccion(conjuntoA, conjuntoB):
    print("2.Interseccion entre conjuntos:\n")
    
    listar_conjuntos(conjuntoA, conjuntoB)

    conjuntoI = conjuntoA & conjuntoB
    print(f"A ∩ B = {conjuntoI}")
    print("N(A ∩ B) = ",len(conjuntoI))
    print()