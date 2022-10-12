
# Ejercicio 01:
import math
radio = int(input("introduce el radio : "))
altura = int(input("introduce la altura : "))
volumen = (math.pi * radio * radio * altura) / 3
print("el volumen del cono es : ", volumen)


"""

# Ejercicio 02:
lista_original = [7, 6, -9, 234, -4, 0, -7]
Positivos = []
Negativos = []
for num in lista_original:
    if num != 0:
        if num > 0:
            Positivos.append(num)
        else:
            Negativos.append(num)

print("Lista Original",lista_original)
print("Positivos",Positivos)
print("Negativos", Negativos)





# Ejercicio 03:
def cuadradosComp(l):
    a = [ a * a for a in l ]
    return a

def cuadradosBucl(l):
    a = []
    for num in l :
        a.append(num*num)
    return a

print("Con el primer met",cuadradosComp([4,1,5.2,3,8]))
print("Con el segundo met",cuadradosBucl([4,1,5.2,3,8]))

"""

