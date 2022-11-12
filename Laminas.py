# -- coding: utf-8 --

#1
def tipodelamina(i):
    salida = []
    for lamina in i:
        if lamina not in salida:
            salida.append(lamina)
    return salida

"""i = ['accion','magia','batalla','batalla','batalla','accion','magia','batalla','batalla','batalla'] """

print(tipodelamina(i))

#2
def mefaltandeltipodelamina(laminasfaltantes,tiposdelamina,untipodelammina):
    salida = []

    for i in laminasfaltantes:
        if tiposdelamina[i] == untipodelammina:
            salida.append(i)
    return salida

"""print(mefaltandeltipodelamina([3,6,8], ['accion','magia','batalla','batalla','batalla','accion','magia','batalla','batalla','batalla',],'batalla'))

print(mefaltandeltipodelamina([1,3,6,8],['accion','magia','batalla','batalla','batalla','accion','magia','batalla','batalla','batalla'],'magia'))"""

#3
def notengo(L1, L2):
    salida = []

    for laminas in L1:
        if laminas not in L2:
            salida.append(laminas)
    return salida

#print(notengo([3,5,7,10,15,16],[4,10,5,8]))

#4
def puedocambiar(L1,L2):
    salida1 = 0 # 1, 2, 3, 4
    salida2 = 0 # 1, 2
    for laminas in L1:
        if laminas not in L2:
            salida1 += 1
    
    for laminas in L2:
        if laminas not in L1:
            salida2 += 1
    return min(salida1, salida2)

#print(puedocambiar([3,5,7,10,15,16],[4,10,5,8]))