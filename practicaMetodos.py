texto = "Bievenidos al putedeadero"

print(texto.lower())
print(texto.upper())
print(texto.title())

print(texto.find("al"))
print(texto.count("e"))

textoFinal = texto.replace("e", "3")
print(textoFinal)

valor = texto.isnumeric()
print(valor)

cadenaSeparada = texto.split(" ")
print(cadenaSeparada)
