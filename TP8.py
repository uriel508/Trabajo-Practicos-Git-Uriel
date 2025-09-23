from collections import deque

class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        return self.items

    #Ejercicio 1
    def invertir(self):
        invertida = []
        while not self.esta_vacia():
            invertida.append(self.pop())
        return invertida

    #Ejercicio 2
    def invertir_palabra(self, palabra):
        pila = list(palabra)
        invertida = ""
        while pila:
            invertida += pila.pop()
        return invertida

    #Ejercicio 3
    def es_palindromo(self, palabra):
        pila = list(palabra)
        invertida = "".join(reversed(pila))
        return palabra == invertida

    #Ejercicio 4
    def camino(self, pueblos):
        pila = []
        print("IDA:")
        for p in pueblos:
            print(p, end=" -> ")
            pila.append(p)
        print("\nVUELTA:")
        while pila:
            print(pila.pop(), end=" -> ")
        print()

    #Ejercicio 5
    def balanceado(self, cadena):
        pila = []
        for c in cadena:
            if c == "(":
                pila.append(c)
            elif c == ")":
                if not pila:
                    return "Error: falta ("
                pila.pop()
        return "Correcto" if not pila else "Error: falta )"

    #Ejercicio 6
    def retirar_contenedor(self, pila, id_retirar):
        aux = []
        while pila and pila[-1] != id_retirar:
            aux.append(pila.pop())
        if not pila:
            return "Contenedor no encontrado"
        pila.pop()  # Retiro el buscado
        while aux:
            pila.append(aux.pop())
        return pila

    #Ejercicio 7
    def invertir_archivo(self, entrada, salida):
        with open(entrada, "r") as f:
            lineas = f.readlines()
        with open(salida, "w") as f:
            for linea in reversed(lineas):
                f.write(linea)

    #Ejercicio 8
    def invertir_frase(self, frase):
        palabras = frase.split()
        pila = palabras[::-1]
        return " ".join(pila)


class Cola:
    def __init__(self):
        self.items = deque()

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        return list(self.items)

    #Ejercicio 9
    def sala_espera(self, pacientes):
        cola = deque(pacientes)
        con_obra_social = 0
        while cola:
            nombre, obra = cola.popleft()
            print(f"Atendiendo a {nombre}")
            if obra:
                con_obra_social += 1
        return con_obra_social

    #Ejercicio 10
    def correo(self, clientes, max_cartas=5):
        cola = deque(clientes)
        while cola:
            persona, cartas = cola.popleft()
            entregar = min(cartas, max_cartas)
            print(f"{persona} entrega {entregar} cartas")
            if cartas > max_cartas:
                cola.append((persona, cartas - max_cartas))

    #Ejercicio 11
    def cola_impresion(self, documentos):
        cola = deque(documentos)
        while cola:
            doc = cola.popleft()
            print(f"Imprimiendo {doc['documento']} ({doc['paginas']} páginas)")

#MENU
def menu():
    pila_obj = Pila()
    cola_obj = Cola()

    while True:
        print("""
        \n          MENU
        1. Invertir pila de 3 elementos
        2. Invertir palabra con pila
        3. Verificar palíndromo con pila
        4. Camino ida y vuelta
        5. Balancear paréntesis
        6. Retirar contenedor específico
        7. Invertir líneas de un archivo
        8. Invertir orden de palabras en frase
        9. Sala de espera (cola FIFO)
        10. Cola de correo
        11. Cola de impresión
        0. Salir
        """)
        opcion = input("Elija una opción: ")

        if opcion == "1":
            pila = Pila()
            for i in [1, 2, 3]:
                pila.push(i)
            print("Pila original:", pila.mostrar())
            print("Pila invertida:", pila.invertir())

        elif opcion == "2":
            palabra = input("Ingrese una palabra: ")
            print("Invertida:", pila_obj.invertir_palabra(palabra))

        elif opcion == "3":
            palabra = input("Ingrese una palabra: ")
            print("Es palíndromo?", pila_obj.es_palindromo(palabra))

        elif opcion == "4":
            pueblos = input("Ingrese pueblos separados por coma: ").split(",")
            pila_obj.camino(pueblos)

        elif opcion == "5":
            cadena = input("Ingrese una cadena con paréntesis: ")
            print(pila_obj.balanceado(cadena))

        elif opcion == "6":
            pila = [1, 2, 3, 4, 5]
            print("Pila inicial:", pila)
            id_retirar = int(input("Ingrese ID a retirar: "))
            print("Nueva pila:", pila_obj.retirar_contenedor(pila, id_retirar))

        elif opcion == "7":
            entrada = input("Archivo de entrada: ")
            salida = input("Archivo de salida: ")
            pila_obj.invertir_archivo(entrada, salida)
            print("Archivo invertido creado.")

        elif opcion == "8":
            frase = input("Ingrese una frase: ")
            print("Invertida:", pila_obj.invertir_frase(frase))

        elif opcion == "9":
            pacientes = [("Ana", True), ("Luis", False), ("Marta", True)]
            print("Con obra social:", cola_obj.sala_espera(pacientes))

        elif opcion == "10":
            clientes = [("Juan", 7), ("Ana", 3), ("Luis", 10)]
            max_cartas = int(input("Máximo de cartas por persona: "))
            cola_obj.correo(clientes, max_cartas)

        elif opcion == "11":
            documentos = [
                {"documento": "Trabajo1.pdf", "paginas": 5},
                {"documento": "CV.docx", "paginas": 2},
                {"documento": "Informe.doc", "paginas": 10}
            ]
            cola_obj.cola_impresion(documentos)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()
