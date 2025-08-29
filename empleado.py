class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calculo_salario(self):
        return self.horas_trabajadas * self.tarifa_hora
