listaNumeros = []

def sumaValores (*numeros:int):
    for numero in numeros:
        listaNumeros.append(numero)
    print(listaNumeros)
    suma = sum(listaNumeros)
    print(suma)
    
sumaValores(5, 3)

