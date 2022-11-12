def FuncionIntercambiemos(L1,l2):
    salida1 = 0
    salida2 = 0
    for elemeto in L1:
        if elemeto not in L2:
            salida1 += 1
    
    for elemeto in L2:
        if elemeto not in L1:
            salida2 += 1
    return min(salida1, salida2)

L1 = ["Balón","Carrito","Muñeca","Dominó","Corneta","Avión","Oso","Cartas"] # Nintendo Perrito Flechas

L2 = ["Nintendo","Muñeca","Perrito","Oso","Balón","Avión","Flechas"]# carrito Domino Corneta Cartas 

print(FuncionIntercambiemos(L1,L2))