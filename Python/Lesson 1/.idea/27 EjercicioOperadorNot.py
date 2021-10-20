#Este ejercicio es igual que el anterior pero vamos a invertir la logica con el operador NOT
vacaciones = False
diaDescanso = False

if not (vacaciones or diaDescanso):
    print("Tiene deberes por hacer")
else:
    print("Puede asistir al juego")