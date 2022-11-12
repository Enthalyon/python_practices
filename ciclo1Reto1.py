a = int(input("Digite un peso en gramos: "))

b = (a*2)+4

c = int((a+b)/5)

def cantidad(sustancia_c):
    if sustancia_c < 0:
        brebaje = "error, ha ingresado un valor incorrecto" 
    elif sustancia_c >= 0 and sustancia_c  <= 20:
        print(a, b, c)
        brebaje = "uno"
    elif sustancia_c >= 21 and sustancia_c <= 40:
        print(a, b, c)
        brebaje = "dos"
    elif sustancia_c >= 41 and sustancia_c <= 80:
        print(a, b, c)
        brebaje = "tres"
    else:
        print(a, b, c)
        brebaje = "cuatro"
    
    return brebaje

print(cantidad(c))