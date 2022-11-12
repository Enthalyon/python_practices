def FuncionProductos(A):
    salida = []
    for elemento in A:
        if elemento not in salida:
            salida.append(elemento)
    return salida

A = ["Balón","Carrito","Muñeca","Dominó","Balón","Muñeca","Corneta","Avión","Carrito"]

print(FuncionProductos(A))
