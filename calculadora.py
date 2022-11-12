# Haga un programa en python que permita al usuario escoger el tipo de operación
# que desea realizar (suma, resta, multiplicación y division)
# entrada un número para definir el tipo de operación y dos números a y b que se operaran
# salida el resultado de la operación

operacion = int(input("Menú\n1.Suma\n2.Resta\n3.Multiplicación\n4.División\n"))


if operacion == 1:
    a = float(input("ingrese un numero: "))
    b = float(input("ingrese un numero: "))
    resultado = print(a+b)
elif operacion == 2:
    a = float(input("ingrese un numero: "))
    b = float(input("ingrese un numero: "))
    resultado = print(a-b)
elif operacion == 3:
    a = float(input("ingrese un numero: "))
    b = float(input("ingrese un numero: "))
    resultado = print(a*b)
elif operacion == 4 and b >0:
    a = float(input("ingrese un numero: "))
    b = float(input("ingrese un numero: "))
    resultado = print(a/b)
else:
    print("Ha ingresado un valor incorrecto")
