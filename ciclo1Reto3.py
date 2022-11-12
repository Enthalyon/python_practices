contador = 1
salida1 = ""
salida2 = ""

resultadosDado = input("Ingrese los resultados de los dados lanzados: ").split(" ")

for a in range(len(resultadosDado)):
    if (a + 1) != len(resultadosDado):
        if resultadosDado[a] == resultadosDado[a + 1]:
            contador += 1
        if resultadosDado[a] != resultadosDado[a + 1]:
            salida2 += str(contador) + " "
            contador = 1
            salida1 += resultadosDado[a] + " "
    elif ((a + 1) == len(resultadosDado)):
        salida2 += str(contador)
        contador = 1
        salida1 += resultadosDado[a]  

print(salida1)
print(salida2)