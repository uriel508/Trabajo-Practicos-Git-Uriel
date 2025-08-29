from alumno import Alumno
from triangulo import Triangulo
from persona import Persona
from planeta import Planeta
from vehiculo import Vehiculo
from empleado import Empleado
from collections import Counter

#Alumno 
print("===== Alumno =====")
a1 = Alumno("Juan", 8)
a2 = Alumno("Ana", 4)
a1.imprimir(); a1.resultado()
a2.imprimir(); a2.resultado()

# Triángulo 
print("\n===== Triángulos =====")
t1 = Triangulo(3, 4, 5)
t2 = Triangulo(5, 5, 5)
for t in [t1, t2]:
    print(f"Lados: {t.lado1}, {t.lado2}, {t.lado3}")
    print(f"Perímetro: {t.perimetro()}")
    print(f"Área: {t.area()}")
    print(f"Forma: {t.forma()}")

#Persona 
print("\n===== Personas =====")
p1 = Persona("Carlos", "Pérez", 20, "12345678")
p2 = Persona("Lucía", "Gómez", 15, "87654321")
for p in [p1, p2]:
    p.mostrar()
    print("Mayor de edad:", p.esMayorDeEdad())

#Planetas 
print("\n===== Planetas =====")
pl1 = Planeta("Tierra", 1, 5.97e24, 1.08e12, 12742, 149597870, "Rocoso", True)
pl2 = Planeta("Júpiter", 79, 1.90e27, 1.43e15, 139820, 778500000, "Gaseoso", True)
for pl in [pl1, pl2]:
    pl.mostrar()
    print(f"Densidad: {pl.densidad()} kg/km³")
    print("Es exterior:", pl.es_exterior())

#Vehículos
print("\n===== Vehículos =====")
vehiculos = [
    Vehiculo("Ford", "Fiesta", "AA123BB", "Rojo"),
    Vehiculo("Chevrolet", "Onix", "CC456DD", "Azul"),
    Vehiculo("Ford", "Focus", "EE789FF", "Negro")
]
marcas = [v.marca for v in vehiculos]
conteo = Counter(marcas)
print("Marcas de la familia:", marcas)
print("Conteo por marca:", conteo)

#Empleados
print("\n===== Empleados =====")
empleados = [
    Empleado("Mario", 40, 10),
    Empleado("Laura", 35, 12)
]
for e in empleados:
    print(f"{e.nombre} cobra: ${e.calculo_salario()}")
