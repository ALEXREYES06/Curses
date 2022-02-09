class rectangulo:
    def __init__(self, alturaRectangulo, baseRectangulo):
        self.alturaRectangulo = alturaRectangulo
        self.baseRectangulo = baseRectangulo
    
    def calculaArea (self):
        return self.baseRectangulo * self.alturaRectangulo

<<<<<<< HEAD
alturaRectangulo = int(input(f'Ingrese la altura del rectángulo: '))
baseRectangulo = int(input (f'Ingrese la base del rectángulo: '))
=======
alturaRectangulo = int( input(f'Ingrese la altura del rectángulo: '))
baseRectangulo = int( input (f'Ingrese la base del rectángulo: '))
>>>>>>> 0be86acc8de0678eb0c92aafb7b717c5ede6d0ca

areaRectangulo = rectangulo(alturaRectangulo, baseRectangulo)
print(f'El área del Rectángulo es: {areaRectangulo.calculaArea()}')

