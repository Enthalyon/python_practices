def valor_absoluto(x):
    if x >= 0:
        valor = x
    else:
        valor = -x
    return valor

a = int(input("Escriba valor:"))

resultado = valor_absoluto(a)
print("El valor absoluto es ", resultado)
