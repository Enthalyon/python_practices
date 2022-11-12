import json
salida1 = 0
salida2 = ""
stockJson = input("Ingrese el stock de la tienda: ")
#stockJson = """{"Whisky": 20, "Aguardiente": 30, "Cerveza": 27, "Vodka": 16}"""
pedido = input("ingrese los licores que desea: ").split(" ")
#pedido = "Aguardiente Tequila Vodka".split(" ")

stock = json.loads(stockJson)

for i in range(len(pedido)):
    if pedido[i] in stock.keys():
      salida1 += stock.get(pedido[i], "")
      salida2 += pedido[i]
      if (i+1) != len(pedido):
        salida2 += " "

print(salida1)
print(salida2)