edad = int(input("por favor ingresa tu edad: "))

casoNiño =  edad > 0 and edad <11 
casoAdolescente = edad > 10 and edad < 21
casoAdulto = edad > 20 and edad < 31

if casoNiño:
    print ("Nalgas miadas socroso")
elif casoAdolescente:
    print("bajale a tus hormonas, no seas caliente")
elif casoAdulto:
    print ("Huye, la vida es no como piensas")
else:
    print("Eres un dinosaurio, ya mátate.")
