# -- coding: utf-8 --

#Funcióm 1
def Productos(A):
    salida = []
    for elemento in A:
        if elemento not in salida:
            salida.append(elemento)
    return salida

"""A = ["Balón","Carrito","Muñeca","Dominó","Balón","Muñeca","Corneta","Avión","Carrito"]

print(Productos(A))"""


#función 2
def Faltante(L,M,N):
    salida = []

    for i in L:
        if M[i] == N:
            salida.append(i)
    return salida

"""L = [2, 0, 5, 1, 3]
M = ["Dominó","Balón","Muñeca","Balón","Corneta","Avión"]
N = "Balón"
print(Faltante(L,M,N))"""


#Función 3
def TeFaltan(L1, L2):
    salida = []

    for elemento in L1:
        if elemento not in L2:
            salida.append(elemento)
    return salida

"""L1 = ["Balón","Carrito","Muñeca","Dominó","Corneta","Avión","Oso"]
L2 = ["Muñeca","Perrito","Oso","Balón","Avión"]

print(TeFaltan(L1,L2))"""


#Función 4
def Intercambiemos(L1,L2):
    salida1 = 0
    salida2 = 0
    for elemeto in L1:
        if elemeto not in L2:
            salida1 += 1
    
    for elemeto in L2:
        if elemeto not in L1:
            salida2 += 1
    return min(salida1, salida2)

"""L1 = ["Balón","Carrito","Muñeca","Dominó","Corneta","Avión","Oso","Cartas"] # Nintendo Perrito Flechas

L2 = ["Nintendo","Muñeca","Perrito","Oso","Balón","Avión","Flechas"]# carrito Domino Corneta Cartas 

print(Intercambiemos(L1,L2))"""