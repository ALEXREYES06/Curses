class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle (self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Juan', 'Perez', 28)
persona1.mostrar_detalle()
persona1.telefono = '4772849517'
#Persona.mostrar_detalle(persona1)

persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()