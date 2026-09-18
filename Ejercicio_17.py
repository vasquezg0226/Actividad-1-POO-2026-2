import math


class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular(self):
        self.area = math.pi * self.radio ** 2
        self.longitud = 2 * math.pi * self.radio

    def mostrar(self):
        print("El área del círculo es:", self.area)
        print("La longitud de la circunferencia es:", self.longitud)



radio = float(input("Ingrese el radio del círculo: "))

circulo = Circulo(radio)

circulo.calcular()

circulo.mostrar()
