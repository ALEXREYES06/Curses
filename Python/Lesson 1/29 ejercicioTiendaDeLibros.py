bienvenida = """
                        a
                       aaa
                     aaaaaa
                    aaa  aaa
                   aaa    aaa
                  aaaaaaaaaaaa
                 aaaaaaaaaaaaaa
                aaaaa      aaaaa
               aaaaa        aaaaa
----------------------------------------------------------
          --Bienvenido a librería virtual--
por favor, ingresa los datos que se piden a continuación."""

print(bienvenida)

nombreLibro = str(input("Ingresa el nombre del libro: "))
idLibro = int(input("ingresa el ID del libro: "))
precioLibro = float((input("ingresa el precio del libro en formato de pesos y centavos M.N/00:$ ")))
envioLibro = (input("¿El envio del libro es gratuito? Si/ No : " ))

if envioLibro == "Si":
    envioLibro = "Gratis"
elif envioLibro == "No":
    envioLibro = "Por cobrar"
else:
    envioLibro = "Valor incorrecto, debe ingresar, 'Si', o 'No'"

print(f"""
    El nombre del libro es: {nombreLibro}.
    El ID del libro es {idLibro}.
    El precio del libro es: {precioLibro}.
    El envío del libro será:  {envioLibro}.
    """)