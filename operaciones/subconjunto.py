def subconjunto(conjuntoA, conjuntoB):
    print("5.Comprobar si es un subconjunto\n")
    if conjuntoA.issubset(conjuntoB) :
        print("A es subconjunto de B")
    elif conjuntoB.issubset(conjuntoA) :
        print("B es subconjunto de A")
    else :
        print("No existen subconjuntos")