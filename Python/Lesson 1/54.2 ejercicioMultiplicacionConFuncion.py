import operator
import functools
listaNumeros = []

def multiplicaValores (*numeros:int):
    for numero in numeros:
        listaNumeros.append(numero)
    print(listaNumeros)
    multiplicacion = functools.reduce(operator.mul, listaNumeros)
    print(multiplicacion)
    
multiplicaValores(5, 3, 2, 5)