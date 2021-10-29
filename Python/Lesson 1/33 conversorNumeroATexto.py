numero = int(input("Ingresa un numero entre 1 y 3: "))
numeroTexto = ""

if numero == 1:
    numeroTexto = "Número Uno"
elif numero == 2:
    numeroTexto = "Número Dos"
elif numero == 3:
    numeroTexto = "Número Tres"
else:
    numeroTexto = "Valor fuera de rango"

print(f"El número proporcionado es: ({numero}), {numeroTexto}")