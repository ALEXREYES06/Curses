class rectangulo:
    def __init__(self, alturaRectangulo, baseRectangulo):
        self.alturaRectangulo = alturaRectangulo
        self.baseRectangulo = baseRectangulo
    
    def calculaArea (self):
        return self.baseRectangulo * self.alturaRectangulo

alturaRectangulo = int(input(f'Ingrese la altura del rectángulo: '))
baseRectangulo = int(input (f'Ingrese la base del rectángulo: '))

areaRectangulo = rectangulo(alturaRectangulo, baseRectangulo)
print(f'El área del Rectángulo es: {areaRectangulo.calculaArea()}')
