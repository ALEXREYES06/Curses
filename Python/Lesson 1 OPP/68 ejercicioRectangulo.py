class rectangulo:
    def __init__(self, alturaRectangulo, baseRectangulo):
        self.alturaRectangulo = alturaRectangulo
        self.baseRectangulo = baseRectangulo
    
    def calculaArea (self):
        return self.baseRectangulo * self.alturaRectangulo

alturaRectangulo = input(f'Ingrese la altura del rectángulo: ')
baseRectangulo = input (f'Ingrese la base del rectángulo: ')

areaRectangulo = rectangulo()
print(f'El área del Rectángulo es: {areaRectangulo.calculaArea()}')
