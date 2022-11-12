# Este programa simula una calculadora

print()
print("   **** Menú ****")
print()
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print()
opc = input("Seleccione una opción: ")

if opc == "1": # Suma
	print("Usted quiere hacer una suma")
	n1 = float(input("Número 1: "))
	n2 = float(input("Número 2: "))

	print("La suma de los números es", n1+n2)


if opc == "2": # Resta
	print("Usted quiere hacer una resta")
	n1 = float(input("Número 1: "))
	n2 = float(input("Número 2: "))
    print("La resta de los números es", n1-n2)


if opc == "3": # Multiplicación
	print("Usted quiere hacer una Multiplicación")
	n1 = float(input("Número 1: "))
	n2 = float(input("Número 2: "))
	print("La multilicación de los números es", n1*n2)


if opc == "4": # División
	print("Usted quiere hacer una División")
	n1 = float(input("Número 1: "))
	n2 = float(input("Número 2: "))
	if n2 == 0:
		print("No se puede dividir por cero")
		input("Enter para continuar...")
		exit()

	print("La división de los números es", n1/n2)	

if opc != "1" and opc != "2" and opc != "3" and opc != "4":
	print("Opción no válida")

input("Pausa...")