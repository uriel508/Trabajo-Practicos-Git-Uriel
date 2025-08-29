class Persona:
    def __init__(self, nombre="", apellido="", edad=0, dni=""):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print(f"Nombre: {self.nombre} {self.apellido}, Edad: {self.edad}, DNI: {self.dni}")

    def esMayorDeEdad(self):
        return self.edad >= 18
