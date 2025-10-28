import random
import os

#Ejercicio 1
def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

numeros1 = [76, 21, 34, 68, 31, 27, 53]
print("Ordenacion por Insercion:")
print("Original:", numeros1)
print("Ordenado:", insertion_sort(numeros1.copy()))

#Ejercicio 2
def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

numeros2 = [6, 2, 4, 8, 3, 7, 5]
print("Ordenacion por Seleccion:")
print("Original:", numeros2)
print("Ordenado:", selection_sort(numeros2.copy()))

#Ejercicio 3
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print("Ingreso de 6 numeros por el usuario:")
usuario = []
for i in range(6):
    num = int(input(f"Ingrese el número {i + 1}: "))
    usuario.append(num)

print("Original:", usuario)
print("Ordenado por Inserción:", insertion_sort(usuario.copy()))
print("Ordenado por Selección:", selection_sort(usuario.copy()))
print("Ordenado por Burbuja:", bubble_sort(usuario.copy()))

#Ejercicio 4
numeros_archivo = [random.randint(1, 1000) for _ in range(50)]

with open("nros.txt", "w") as f:
    for num in numeros_archivo:
        f.write(str(num) + "\n")

numeros_ordenados = insertion_sort(numeros_archivo.copy())

with open("ordenado.txt", "w") as f:
    for num in numeros_ordenados:
        f.write(str(num) + "\n")

print("Archivo 'nros.txt' generado y ordenado en 'ordenado.txt'")


#Ejercicio 5
def insertion_sort_array_simulada(lista):
    # Simula un array simplemente usando una lista
    copia = lista.copy()
    insertion_sort(copia)
    return copia

arr = [10, 5, 3, 12, 7, 2]
print("Ordenación tipo 'array':")
print("Original:", arr)
arr_ordenado = insertion_sort_array_simulada(arr)
print("Ordenado:", arr_ordenado)

#Ejercicio 6
numeros_random = [random.randint(1, 100) for _ in range(10)]
print("Numeros aleatorios:", numeros_random)
print("Inserción:", insertion_sort(numeros_random.copy()))
print("Selección:", selection_sort(numeros_random.copy()))
print("Burbuja:", bubble_sort(numeros_random.copy()))


#Ejercicio 7
print("ORDENAR PRECIOS DE GOLOSINAS")
precios = []
for i in range(10):
    precio = float(input(f"Ingrese el precio de la golosina {i+1}: $"))
    precios.append(precio)

print("Precios originales:", precios)
print("Ordenados por Inserción:", insertion_sort(precios.copy()))
print("Ordenados por Selección:", selection_sort(precios.copy()))


#Ejercicio 8
print("LISTA Y ARRAY ALEATORIOS")

lista_random = [random.randint(1, 100) for _ in range(6)]
array_random = lista_random.copy() 

print("Lista original:", lista_random)
print("Array original:", array_random)

print("Lista ordenada (Burbuja):", bubble_sort(lista_random.copy()))
print("Array ordenado (Selección):", selection_sort(array_random.copy()))


#Ejercicio 9
print("MATRIZ 4x6 ORDENADA POR FILAS")

filas, columnas = 4, 6
matriz = [[random.randint(0, 9) for _ in range(columnas)] for _ in range(filas)]

print("Matriz original:")
for fila in matriz:
    print(fila)

for fila in matriz:
    insertion_sort(fila)

print("Matriz ordenada por filas:")
for fila in matriz:
    print(fila)


#Ejercicio 10
print("PACIENTES ORDENADOS POR EDAD")

if not os.path.exists("pacientes.txt"):
    ejemplo = [
        "Sanchez, Luis, 64, OSDE\n",
        "Balaz, Sara, 32, OSECAD\n",
        "Lipa, Julieta, 27, OSDE\n",
        "Perez, Lucila, 30, OSECAD\n"
    ]
    with open("pacientes.txt", "w", encoding="utf-8") as f:
        f.writelines(ejemplo)
    print("Archivo 'pacientes.txt' creado con datos de ejemplo.")

with open("pacientes.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()

pacientes = []
for linea in lineas:
    datos = [dato.strip() for dato in linea.split(",")]
    apellido, nombre, edad, obra_social = datos[0], datos[1], int(datos[2]), datos[3]
    pacientes.append((apellido, nombre, edad, obra_social))

pacientes.sort(key=lambda x: x[2])

print("Pacientes ordenados por edad:")
for p in pacientes:
    print(f"{p[0]}, {p[1]}, {p[2]}, {p[3]}")

with open("pacientes_por_edad.txt", "w", encoding="utf-8") as f:
    for p in pacientes:
        f.write(f"{p[0]}, {p[1]}, {p[2]}, {p[3]}\n")

print("Archivo 'pacientes_por_edad.txt' generado correctamente.")

#Ejercicio 11
notas = []

for i in range(10):
    nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
    notas.append(nota)

peor = mejor = notas[0]

for n in notas:
    if n < peor:
        peor = n
    if n > mejor:
        mejor = n

print(f"La peor nota es: {peor}")
print(f"La mejor nota es: {mejor}")

#Ejercicio 12
nombres = ["Legolas", "Sam", "Frodo", "Sauron", "Gollum"]

for i in range(len(nombres)):
    for j in range(0, len(nombres)-i-1):
        if len(nombres[j]) > len(nombres[j+1]):
            nombres[j], nombres[j+1] = nombres[j+1], nombres[j]

print("Nombres ordenados por longitud:", nombres)

#Ejercicio 13
pequeña = [random.randint(1, 100) for _ in range(10)]
grande = [random.randint(1, 1000000) for _ in range(6000000)]

print("LISTA PEQUEÑA (10 numeros)")
print("Lista original pequeña:", pequeña)

print("Bubble sort:", bubble_sort(pequeña))
print("Insertion sort:", insertion_sort(pequeña))
print("Python sort:", sorted(pequeña))

resultado_burbuja = bubble_sort(pequeña)
resultado_insercion = insertion_sort(pequeña)
resultado_sorted = sorted(pequeña)

print("¿Todos los metodos dan el mismo resultado?")
print("Bubble == Insercion:", resultado_burbuja == resultado_insercion)
print("Bubble == Python sort:", resultado_burbuja == resultado_sorted)

print("LISTA GRANDE (6,000,000 numeros)")
print("Ordenando lista grande con Python sort")
resultado_grande = sorted(grande)
print("Python sort completado - primeros 5:", resultado_grande[:5])
print("Python sort completado - últimos 5:", resultado_grande[-5:])

print("COMPARACION CON SUBCONJUNTOS PEQUEÑOS")
subgrande_1000 = grande[:1000]

print("Con 1000 elementos:")
print("Bubble sort:", bubble_sort(subgrande_1000)[:10], "...")
print("Insertion sort:", insertion_sort(subgrande_1000)[:10], "...")

print("CONCLUSION")
print("Para lista pequeña: todos los algoritmos funcionan bien")
print("Para lista grande (6M): solo Python sorted() es practico")
print("Bubble sort e Insertion sort son muy lentos para listas grandes")
print("Python sorted() usa Timsort (híbrido) que es mas eficiente")