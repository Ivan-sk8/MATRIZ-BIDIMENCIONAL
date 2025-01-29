#Ejercicio5
array = [
    [1, 2, 3],
    [4, 5, 6]
]
print()
print()
print()
print("Ejercicio 5")
def crearMatrizMporN(m, n, valorInicial):
    matriz2 = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append(valorInicial)
        matriz2.append(fila)

    return matriz2

matriz2 = crearMatrizMporN(3,4,5)
for fila in matriz2:
    print(fila)

#Ejercicio6
print()
print()
print()
print("Ejercicio 6")
matriz_transpuesta = []
for i in range(len(array[0])):
    fila_transpuesta = []
    for j in range(len(array)):
        fila_transpuesta.append(array[j][i])
    matriz_transpuesta.append(fila_transpuesta)

for fila in matriz_transpuesta:
    print(fila)


#Ejercicio 7
print()
print()
print()
print("Ejercicio 7")
array7 = [
    [23, 45, 43, 23, 45],
    [45, 67, 54, 32, 45],
    [89, 90, 87, 65, 44],
    [23, 45, 67, 32, 10]
]
def sumarArray(array7):
    sumaTotal = 0
    for fila in array7:
        for valor in fila:
            sumaTotal = valor + sumaTotal
    return sumaTotal

arraySumado = sumarArray(array7)
print(arraySumado)




#Ejercicio 9
print()
print()
print()
print("Ejercicio 9")

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
def buscarEnMatriz(matrix, valor):
    for fila in matrix:
        if valor in fila:
            return True
        return False
    
print(buscarEnMatriz(matrix, 5))