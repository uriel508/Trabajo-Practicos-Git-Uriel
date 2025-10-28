import random

# Ejercicio 1
def ejercicio1():
    lista_numeros = [random.randint(1, 100) for _ in range(10)]
    print("Lista generada:", lista_numeros)
    
    numero = int(input("Ingrese un número a buscar: "))
    encontrado = False
    posicion = -1
    
    # Busqueda lineal
    for i in range(len(lista_numeros)):
        if lista_numeros[i] == numero:
            encontrado = True
            posicion = i
            break
    
    if encontrado:
        print(f"El número {numero} se encuentra en la posición {posicion}")
    else:
        print(f"El número {numero} no se encuentra en la lista")

print("EJERCICIO 1")
ejercicio1()

# Ejercicio 2
def ejercicio2():
    alumnos = ["Ana", "Luis", "María", "Carlos", "Sofía", "Pedro", "Laura", "Diego"]
    print("Lista de alumnos:", alumnos)
    nombre = input("Ingrese el nombre del alumno a buscar: ")
    encontrado = False
    for alumno in alumnos:
        if alumno.lower() == nombre.lower():
            encontrado = True
            break
    
    if encontrado:
        print(f"El alumno {nombre} SÍ se presentó al examen")
    else:
        print(f"El alumno {nombre} NO se presentó al examen")

print("EJERCICIO 2")
ejercicio2()

# Ejercicio 3
def busqueda_lineal_completa(lista, valor):
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == valor:
            posiciones.append(i)
    return posiciones

def ejercicio3():
    lista = [5, 2, 8, 2, 9, 1, 2, 7, 2]
    print("Lista:", lista)
    
    valor = int(input("Ingrese el valor a buscar: "))
    posiciones = busqueda_lineal_completa(lista, valor)
    
    if posiciones:
        print(f"El valor {valor} se encontró en las posiciones: {posiciones}")
        print(f"Total de ocurrencias: {len(posiciones)}")
    else:
        print(f"El valor {valor} no se encontró en la lista")

print("EJERCICIO 3")
ejercicio3()

# Ejercicio 4
def ejercicio4():
    # Pedir intervalo
    a = int(input("Ingrese el límite inferior (a): "))
    b = int(input("Ingrese el límite superior (b): "))
    
    if a >= b:
        print("Error: a debe ser menor que b")
        return
    
    print(f"\nPiense un número entre {a} y {b}")
    print("Responda con: 'mayor', 'menor', 'igual' o 'salir'")
    intentos = 0
    minimo = a
    maximo = b
    
    while True:
        # Busqueda binaria para adivinar
        intento = (minimo + maximo) // 2
        intentos += 1
        
        respuesta = input(f"\n¿Es {intento}? ").lower()
        
        if respuesta == "igual":
            print(f"Adivine, El número es {intento}")
            print(f"Lo logre en {intentos} intentos")
            break
        elif respuesta == "mayor":
            minimo = intento + 1
        elif respuesta == "menor":
            maximo = intento - 1
        elif respuesta == "salir":
            print("Juego terminado por el usuario")
            break
        else:
            print("Respuesta no válida. Use: 'mayor', 'menor', 'igual' o 'salir'")
        
        if minimo > maximo:
            print("¡Estás haciendo trampa! El número no está en el intervalo")
            break

print("EJERCICIO 4")
ejercicio4()