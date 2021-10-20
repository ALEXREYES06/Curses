#
edad = int(input("Ingresa la edad de la persona: "))
edadMinimaVeintes = 20
edadMaximaVeintes = 29
edadMinimaTreintas = 30
edadMaximaTreintas = 39

dentroDeRangoVeintes = edad >= edadMinimaVeintes and edad <= edadMaximaVeintes
print(dentroDeRangoVeintes) #Este comentario solo imprime el valor de la afirmación
dentroDeRangoTreintas = edad >= edadMinimaTreintas and edad <= edadMaximaTreintas
print(dentroDeRangoTreintas)

if dentroDeRangoVeintes or dentroDeRangoTreintas:
    print(f'La edad {edad} está dentro del rango de los (20\'s) o de los (30\'s)')
    if dentroDeRangoVeintes:
        print("Dentro del rango de los 20's")
    elif dentroDeRangoTreintas:
        print("Dentro del rango de los 30's")
else:
    print(f"La edad {edad} se sale de rango de los (20's) o de los (30's)")