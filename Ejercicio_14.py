class Numero:

    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        self.cuadrado = self.numero ** 2
        self.cubo = self.numero ** 3

    def mostrar(self):
        print("El cuadrado es:", self.cuadrado)
        print("El cubo es:", self.cubo)



numero = float(input("Ingrese un número: "))

n = Numero(numero)

n.calcular()

n.mostrar()
