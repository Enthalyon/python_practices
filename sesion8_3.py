def valor_a_pagar(valor):
	if valor <= 100000:
		descuento = 0
	elif valor > 100000 and valor <= 200000:
		descuento = 0.01
	elif 200000 < valor <= 500000:
		descuento = 0.05
	else:
		descuento = 0.1

	return valor*(1-descuento)


v1 = int(input("Valor en compras: "))
print("Total a pagar =", valor_a_pagar(v1))

v2 = int(input("Valor en compras: "))
print("Total a pagar =", valor_a_pagar(v2))

v3 = int(input("Valor en compras: "))
print("Total a pagar =", valor_a_pagar(v3))

input("pausa...")