class Empleado:

    def __init__(self, horas, valor_hora):
        self.horas = horas
        self.valor_hora = valor_hora
        self.salario_bruto = 0
        self.retencion = 0
        self.salario_neto = 0

    def calcular(self):
        self.salario_bruto = self.horas * self.valor_hora
        self.retencion = self.salario_bruto * 0.125
        self.salario_neto = self.salario_bruto - self.retencion

    def mostrar(self):
        print("Salario bruto:", self.salario_bruto)
        print("Retención en la fuente:", self.retencion)
        print("Salario neto:", self.salario_neto)



empleado = Empleado(48, 5000)

empleado.calcular()

empleado.mostrar()
