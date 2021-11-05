calificacion =  int(input("ingresa la calificacion en un rango de (0 a 10): "))
continuar = None

a = calificacion == 9 or calificacion == 10
b = calificacion  == 8 
c = calificacion == 7
d = calificacion == 6
f = calificacion >= 0 and calificacion < 6


while continuar == True:
    if a:
        print ("A")
    elif b:
        print ("B")
    elif c:
        print ("C")
    elif d:
        print ("D")
    elif f:
        print ("F")
    else:
        print ("Valor fuera de rango ingresa solo de 0 a 10")
        
    continuar = str(input("¿Desea continuar? S/N: "))
    if continuar == "S":
            continuar = True
    elif continuar == "N":
            continuar = False
else:
    print("Fin del programa")





