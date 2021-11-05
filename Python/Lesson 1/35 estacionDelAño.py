mes = input("Ingresa por favor el nombre del mes que desees: " )
numeroDeMes = None
estacion = None

if mes == "Enero" or mes == "enero":
    numeroDeMes = 1
elif mes == "Febrero" or mes == "febrero":
        numeroDeMes = 2
elif mes == "Marzo" or mes == "marzo":
        numeroDeMes = 3
elif mes == "Abril" or mes == "abril":
        numeroDeMes = 4
elif mes == "Mayo" or mes == "mayo":
        numeroDeMes = 5
elif mes == "Junio" or mes == "junio":
        numeroDeMes = 6
elif mes == "Julio" or mes == "julio":
        numeroDeMes = 7
elif mes == "Agosto" or mes == "agosto":
        numeroDeMes = 8
elif mes == "Septiembre" or mes == "septiembre":
        numeroDeMes = 9
elif mes == "Octubre" or mes == "octubre":
        numeroDeMes = 10
elif mes == "Noviembre" or mes == "noviembre":
        numeroDeMes = 11
elif mes == "Diciembre" or mes == "diciembre":
        numeroDeMes = 12
else:
    print("Ingresa el nombre de un mes valido")

print(f"El mes que ingresaste es: {mes}, ({numeroDeMes})")

if numeroDeMes == 12 or numeroDeMes == 1 or numeroDeMes == 2 :
        estacion =  "Invierno"
        print(f"El mes pertenece a la temporada de {estacion}.")
elif numeroDeMes == 3 or numeroDeMes == 4 or numeroDeMes == 5 or numeroDeMes == 6 or numeroDeMes == 7:
        estacion =  "Primavera"
        print((f"El mes pertenece a la temporada de {estacion}."))
elif numeroDeMes == 8 or numeroDeMes == 9:
        estacion =  "Verano"
        print((f"El mes pertenece a la temporada de {estacion}."))
elif numeroDeMes == 10 or numeroDeMes == 11:
        estacion =  "Otoño"
        print((f"El mes pertenece a la temporada de {estacion}."))
        

