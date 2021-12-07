#una función recursiva es mandar a llamar a esa funcion a si misma.
#5! = 5 * 4 * 3 * 1
numeroAFactorizar = int(input('Ingrese un nummero a factorizar: '))
def factorial(numero):
    print(numero)
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

resultado = factorial(numeroAFactorizar)
print(f'El factorial de, {numeroAFactorizar} es: {resultado}')