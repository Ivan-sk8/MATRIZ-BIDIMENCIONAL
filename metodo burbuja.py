# Función para ordenar una fila usando el método burbuja
def burbuja(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:  # Comparar elementos adyacentes
                # Intercambiar si están en el orden incorrecto
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Función para ordenar una matriz usando el método burbuja
def ordenar_matriz(matriz):
    for fila in matriz:
        burbuja(fila)  # Ordenar cada fila de la matriz

# Matriz de ejemplo
matriz = [[3, 1, 2], [6, 4, 5], [9, 7, 8]]

# Ordenar la matriz
ordenar_matriz(matriz)

# Imprimir la matriz resultante
print("Matriz ordenada:")
for fila in matriz:
    print(fila)
