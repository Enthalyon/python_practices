import json
salida1 = 0
salida2 = ""

inventarioJson = input("Ingrese el inventario de la tienda: ")

pedido = input("ingrese las laminas que quiere comprar: ").lower().split(" ")


stock = json.loads(inventarioJson)

for i in range(len(pedido)):
    if pedido[i] in stock.keys():
        salida1 += stock.get(pedido[i], "")
        salida2 += pedido[i]
        if (i+1) != len(pedido):
            salida2 += " "

print(salida1)
print(salida2)