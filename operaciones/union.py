from utilidades import listar_conjuntos

def union (conjuntoA, conjuntoB):
    print("1.Union entre conjuntos:\n")

    listar_conjuntos(conjuntoA, conjuntoB)
    
    conjuntoU = conjuntoA | conjuntoB
    
    print(f"A ∪ B = {conjuntoU}")
    print("N(A ∪ B) = ",len(conjuntoU))
    print()