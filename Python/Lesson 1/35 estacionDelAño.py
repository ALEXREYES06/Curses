mes = str(input("Ingresa por favor el nombre del mes que desees: " ))
numeroDeMes = ""

if mes == "Enero" or "enero":
    numeroDeMes = 1
elif mes == "Febrero" or "febrero":
        numeroDeMes = 2
elif mes == "Marzo" or "marzo":
        numeroDeMes = 3
elif mes == "Abril" or "abril":
        numeroDeMes = 4
elif mes == "Mayo" or "mayo":
        numeroDeMes = 5
elif mes == "Junio" or "junio":
        numeroDeMes = 6
elif mes == "Julio" or "julio":
        numeroDeMes = 7
elif mes == "Agosto" or "agosto":
        numeroDeMes = 8
elif mes == "Septiembre" or "septiembre":
        numeroDeMes = 9
elif mes == "Octubre" or "octubre":
        numeroDeMes = 10
elif mes == "Noviembre" or "noviembre":
        numeroDeMes = 11
elif mes == "Diciembre" or "diciembre":
        numeroDeMes = 12
else:
    print("Ingresa el nombre de un mes valido")

print(f"El mes que ingresaste es: {mes}, ({numeroDeMes})")