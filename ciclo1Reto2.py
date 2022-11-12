PuntajeMio = 0
PuntajeAmigo = 0
salida = ""

yo = str(input("Mi lista de letras: ")).upper()

amigo = str(input("Lista amigo: ")).upper()

invitados = str(input("Lista Iniciales invitados: ")).upper()

for y in range(len(invitados)):
    if invitados[y] in yo:
        PuntajeMio +=1        
    if invitados[y] in amigo:
        PuntajeAmigo +=1
    if PuntajeMio>PuntajeAmigo:
        salida += "1"
    if PuntajeMio<PuntajeAmigo:
        salida += "2"
    if PuntajeMio==PuntajeAmigo:
        salida = salida + "*"

print(salida)