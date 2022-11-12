def FuncionTeFaltan(L1, L2):
    salida = []

    for elemento in L1:
        if elemento not in L2:
            salida.append(elemento)
    return salida

L1 = ["Balón","Carrito","Muñeca","Dominó","Corneta","Avión","Oso"]
L2 = ["Muñeca","Perrito","Oso","Balón","Avión"]

print(FuncionTeFaltan(L1,L2))