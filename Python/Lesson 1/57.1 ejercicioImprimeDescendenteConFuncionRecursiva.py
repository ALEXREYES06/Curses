numeroAImprimir = int(input('Ingrese el mayor numero para la cadena de impresión: '))

def imprimeDescendente (numero):
    print(numero)
    if numero == 1:
        return 1
    else:
        return numero - imprimeDescendente(numero - 1)

imprimeDescendente(numeroAImprimir)