sumar = lambda numero,suma: suma + numero

def calcularSumaElementos(suma =  0):
    while True:
        try:
            cantidadElementos = int(input("Ingrese la cantidad de elementos que desea sumar: "))
            break
        except:
            print("No se ingresó un valor numérico a elementos")
    
    for indice in range(cantidadElementos):
        while True:
            try:
                numero = int(input("Ingrese el número que desea agregar a la suma: "))
                break
            except:
                print("No se ingresó valor numerico a suma")
                
        suma = sumar(numero, suma)
    print(f'La suma de los elementos ingresados es: {suma}')

calcularSumaElementos()