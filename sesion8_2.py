#       Tabla de descuestos
# +---------------------+--------+
# |     <= 100,000      |   0%   |
# | >100,000 <= 200,000 |   1%   |
# | >200,000 <= 500,000 |   5%   |
# |       > 500,000     |  10%   |
# +------------+--------+--------+


valor = int(input("Valor de la compra: "))

if valor <= 100000:
	descuento = 0
elif valor > 100000 and valor <= 200000:
	descuento = 0.01
elif 200000 < valor <= 500000:
	descuento = 0.05
else:
	descuento = 0.1

print("El valor a pagar es", valor*(1-descuento))
input("pausa...")