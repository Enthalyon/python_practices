contador = 1
salida1 = ""
salida2 = ""

#nota = "C,E,a,b,g,c,e,c,B,C,g,b,d,f,B,D,g,e,c,a".upper().split(",")
nota = input("Ingrese las notas: ").upper().split(",")

for a in range(len(nota)):
    if (a + 1) != len(nota):
        if nota[a] == nota[a + 1]:
            contador += 1
        if nota[a] != nota[a + 1]:
            salida2 += str(contador) + " "
            contador = 1
            salida1 += nota[a] + " "
    elif ((a + 1) == len(nota)):
        salida2 += str(contador)
        contador = 1
        salida1 += nota[a]  

print(salida1)
print(salida2)