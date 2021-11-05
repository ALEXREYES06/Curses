import time
contador  = 0 

while contador < 5:
    print(f"Ejecutando ciclo while {contador}")
    contador = contador +1
    time.sleep(1)
else: 
    print("Fin de ciclo") 