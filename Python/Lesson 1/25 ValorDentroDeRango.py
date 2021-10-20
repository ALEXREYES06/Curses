#ejercicio para determnar si un numero está dentro de un rango.
valor = int(input("escribe un valor numerico: "))
valorMinimo = 0
ValorMaximo = 10

dentroDeRango = (valor >= valorMinimo) and (valor <= ValorMaximo) #Este es el comparador de valor qu establece los limites

if dentroDeRango:
    print(f"El valor {valor} está dentro del rango")
else:
    print(f"El valor {valor} esta fuera de rango")

