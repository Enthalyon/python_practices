# Ejemplo 1
texto1 = "Hola"
texto2 = "mundo"
print(texto1 + " " + texto2)

#Ejemplo 2
print("El saludo es: %s %s" % (texto1, texto2))

# Ejemplo 3
saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
print(saludoFinal)

# Ejemplo 4
saludoFinal2 = "saludo: {x} {y}".format(x=texto1, y=texto2)
print(saludoFinal2)

# Ejemplo 5
saludoFinal3 = f"saludo: {texto1} {texto2}"
print(saludoFinal3)
