class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

#Ejercicio 1
    def contar_nodos(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

#Ejercicio 2
    def posicion_nodo(self, dato):
        pos = 0
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return pos
            actual = actual.siguiente
            pos += 1
        return -1

#Ejercicio 3
    def eliminar_penultimo(self):
        if not self.cabeza or not self.cabeza.siguiente:
            return
        anterior = None
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.siguiente:
            anterior = actual
            actual = actual.siguiente
        if anterior is None:
            self.cabeza = self.cabeza.siguiente
        else:
            anterior.siguiente = actual.siguiente

#Ejercicio 4
    def filtrar_impares(self):
        nueva = ListaEnlazada()
        actual = self.cabeza
        while actual:
            if actual.dato % 2 != 0:
                nueva.agregar(actual.dato)
            actual = actual.siguiente
        return nueva

#Ejercicio 5
    def dividir_pos_neg(self):
        positivos = ListaEnlazada()
        negativos = ListaEnlazada()
        actual = self.cabeza
        while actual:
            if actual.dato >= 0:
                positivos.agregar(actual.dato)
            else:
                negativos.agregar(actual.dato)
            actual = actual.siguiente
        return positivos, negativos

#Ejercicio 6
    def eliminar_vocales(self):
        vocales = "aeiouAEIOU"
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.dato in vocales:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
            else:
                anterior = actual
            actual = actual.siguiente

#Ejercicio 7
    def contar_ocurrencias(self, dato):
        contador = 0
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                contador += 1
            actual = actual.siguiente
        return contador

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

#Ejemplos de Prueba
def lista_ejemplo():
    lista = ListaEnlazada()
    for num in [1, 2, 3, 4, 5, -6, -7, 2, 3]:
        lista.agregar(num)
    return lista

lista1 = lista_ejemplo()
print("1))) Cantidad de nodos:", lista1.contar_nodos())

lista2 = lista_ejemplo()
print("2))) Posición del nodo con valor 4:", lista2.posicion_nodo(4))

lista3 = lista_ejemplo()
print("3))) Lista antes de eliminar penúltimo:")
lista3.imprimir()
lista3.eliminar_penultimo()
print("Lista después de eliminar penúltimo:")
lista3.imprimir()

lista4 = lista_ejemplo()
print("4))) Lista con solo impares:")
impares = lista4.filtrar_impares()
impares.imprimir()

lista5 = lista_ejemplo()
positivos, negativos = lista5.dividir_pos_neg()
print("5))) Positivos:")
positivos.imprimir()
print("Negativos:")
negativos.imprimir()

lista6 = ListaEnlazada()
for c in "Programacion":
    lista6.agregar(c)
print("6))) Lista de caracteres antes de eliminar vocales:")
lista6.imprimir()
lista6.eliminar_vocales()
print("Lista después de eliminar vocales:")
lista6.imprimir()

lista7 = lista_ejemplo()
print("7))) Ocurrencias del número 2:", lista7.contar_ocurrencias(2))
