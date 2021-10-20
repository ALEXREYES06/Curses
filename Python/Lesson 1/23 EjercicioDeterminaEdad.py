#Ejercicio para determinar la edad de una persona, usando IF, Else.
edadAdulto = 18 #Pude haber puesto el 18 directo en el el IF pero eso sería hardcodear.

edadPersona = int(input("ingresa la edad de la persona:  "))

if edadPersona > edadAdulto :
    print(f"La persona con edad {edadPersona} ya alcanza el timbre")
else:
    print(f"lapersona con edad {edadPersona} sigue siendo un mocoso")