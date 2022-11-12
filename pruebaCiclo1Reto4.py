import json
from pprint import pprint

contadorprecios = 0
salida1 = ""
salida2 = ""

inventario = {
            "Cerveza":6,
            "Vino":None,
            "Whisky":20,
            "Ron":23,
            "Tequila":None,
            "Aguardiente":30,
            "Vodka":16,
            "Brandi":23,
            "Sangria":24
            } #cada elemento de la lista se llama item estan compuestos por la llave y el valor, las llaves son unicas y no se pueden repetir.

entrada1 = """{"Sangria": 24,"Brandi": 23,"Cerveza": 26,"Ron": 23}""" #encerrar en comillas triples para convertir en stream
#entrada1 = str(input("ingrese los licores y su precio con estructura de diccionario: "))
entrada2 = "Tequila Brandi Ron"
#entrada2 = str(input("productos pedidos por el cliente: ")).split(" ")

data = json.loads(entrada1)
dinero = data.values()
print(data)
"""print(type(dinero))
print(type(data))
print(type(entrada1))
print(type(entrada2))"""
"""data2 = json.loads(entrada2)
print(data2)
print(type(data2))"""

#listaDiccionario = json.dumps(entrada2) 
#data2 = json.loads(listaDiccionario)
#print(data2)
#print(entrada2)
#print(type(data2))

"""salida1 = data2.values()
print(salida1)
salida2 = data2.keys()
print(salida2)"""

"""print(data["Brandi"])
print(len(inventario))
print(inventario.get("Brandi"))"""
"""if data.keys() and data.values() == inventario.keys() and inventario.values():
    print(si)"""
"""if data in inventario
    salida1 = data
    print(salida1)
"""
"""def entradaUno(data):
    if entradaUno in inventario:
        return complex(dct['real'], dct['imag'])"""
"""r = inventario.get{"brandi"}
print(r)"""

#print(type(entrada1))
#print(data)
#print(entrada1)
#print(entrada2)
#print(salida1)
#licor = inventario[]
#precio = inventario[data][1]
#c = inventario.get(precio)
#h = inventario.values()
#print(h)
#j = inventario.keys()
#print(j)
#i = "Cerveza" in inventario
"""if "Cerveza" in inventario:
    if inventario["Cerveza"][: ]"""

#print(i)
#print(type(inventario))
#print(len(inventario))
"""for a in range(len(inventario)):
    if a == data:
        salida1 = inventario.get(data)
        print(salida1)"""
#print(precio)
