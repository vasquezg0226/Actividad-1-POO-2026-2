class Familia:

    def __init__(self, juan):
        self.juan = juan
        self.alberto = (2 * juan) / 3
        self.ana = (4 * juan) / 3
        self.mama = juan + self.alberto + self.ana

    def mostrar_edades(self):
        print("Edad de Juan:", self.juan)
        print("Edad de Alberto:", self.alberto)
        print("Edad de Ana:", self.ana)
        print("Edad de la mamá:", self.mama)


edad_juan = int(input("Ingrese la edad de Juan: "))

familia = Familia(edad_juan)

familia.mostrar_edades()