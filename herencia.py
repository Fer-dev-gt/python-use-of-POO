# Esta sera la "Superclase" la cual heredara sus comportamientos a la "Subclase" (class Cuadrado)
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


# Esta sera la "Subclase"    
class Cuadrado(Rectangulo):  # "La clase Cuadrado extiende a la clase Rectangulo"

    def __init__(self, lado):
        super().__init__(lado, lado) # La función "super()" nos permite tener una refencia directa de la "Superclse" (class Rectangulo)


if __name__ == '__main__':
    rectangulo = Rectangulo(base = 3, altura = 4)
    print(f'El area del rectangulo es: {rectangulo.area()}')

    cuadrado = Cuadrado(lado = 5)
    print(f'El area del cuadrado es: {cuadrado.area()}')  # Aca ejecutamos el método area a pesar que no esta definido en la clase "Cuadrado", debido a que la hereda de la "Superclase" Rectangulo