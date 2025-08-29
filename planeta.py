class Planeta:
    def __init__(self, nombre=None, satelites=0, masa=0.0, volumen=0.0, diametro=0, distancia_sol=0, tipo=None, observable=False):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.observable = observable

    def mostrar(self):
        print(f"Planeta: {self.nombre}, Satélites: {self.satelites}, Masa: {self.masa} kg, "
              f"Volumen: {self.volumen} km³, Diámetro: {self.diametro} km, "
              f"Distancia al Sol: {self.distancia_sol} km, Tipo: {self.tipo}, "
              f"Visible: {self.observable}")

    def densidad(self):
        return self.masa / self.volumen if self.volumen > 0 else 0

    def es_exterior(self):
        UA = self.distancia_sol / 149597870
        return UA > 3.4
