#califica tu día del 1 al 10
print("Hola!! ¿Cómo estuvo tu día? (del 1 al 10)")
calificacion = int(input("Califica del 1 al 10: "))

if calificacion <= 10:
    print("Mi día estuvo de: ", calificacion)
else: 
    calificacion = int(input("ingresa un numero positivo menor a 10:" ))