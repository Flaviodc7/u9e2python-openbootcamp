from functools import reduce

def impares(a):
    if (a % 2 != 0):
        return a

def suma(a, b):
    return a + b

numeros = [2, 5, 7, 9, 20]

#filtrado definiendo función
#filtrado = filter(impares, numeros)

#filtrado con lambda
filtrado = list(filter(lambda x: x % 2 != 0, numeros))

print(list(filtrado))

#suma de Impares con función
#sumaImpares = reduce(suma, filtrado)

#suma de Impares con lambda
sumaImpares = reduce(lambda a, b: a + b, filtrado)

print(sumaImpares)