numero1 = int(input("Ingrese cualquier número entero: "))
numero2 = int(input("Ingrese nuevamente cualquier número entero: "))
print(f"Los numeros ingresados son: {numero1} y {numero2}")

if numero1 > numero2:
    print(f"El numero mayor es: {numero1}")
elif numero2 > numero1:
    print(f"El número mayor es: {numero2}")
else:
    print("Los números son iguales.")