def maxima(a, b):
    if a > b :
        maximo = a
    else:
        maximo = b
            
    return maximo

x = int(input("Valor 1: "))
y = int(input("Valor 2: "))

resultado = maxima(x, y)

print("El valor mayor es", resultado)

input("...")
