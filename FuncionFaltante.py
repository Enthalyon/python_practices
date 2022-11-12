def FuncionFaltante(L,M,N):
    salida = []

    for i in L:
        if M[i] == N:
            salida.append(i)
    return salida

L = [2, 0, 5, 1, 3]
M = ["Dominó","Balón","Muñeca","Balón","Corneta","Avión"]
N = "Balón"
print(FuncionFaltante(L,M,N))
