class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Alumno: {self.nombre}, Nota: {self.nota}")

    def resultado(self):
        if self.nota >= 6:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} ha desaprobado.")
