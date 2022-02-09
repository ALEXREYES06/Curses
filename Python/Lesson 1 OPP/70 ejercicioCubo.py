class Cubo:
    def __init__(self, baseCubo, anchoCubo, profundoCubo):
        self.baseCubo = baseCubo
        self.anchoCubo = anchoCubo
        self.profundoCubo = profundoCubo
    
    def calculaVolumenCubo (self):
        return self.baseCubo * self.anchoCubo * self.profundoCubo
    
baseCubo = int(input(f'Ingrese la base del cubo: '))
anchoCubo = int(input(f'Ingrese el ancho del cubo: '))
profundoCubo = int(input(f'ingrese la profundidad del cubo: '))

volumenCubo = Cubo(baseCubo, anchoCubo, profundoCubo)
print(f'El Volumen del cubo es igual a : {volumenCubo.calculaVolumenCubo()}')
