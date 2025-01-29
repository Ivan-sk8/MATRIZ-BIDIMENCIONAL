# Función para buscar un elemento en la matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

def buscar_elemento(matriz, objetivo):
    for i in range(len(matriz)):  # Recorre las filas
        for j in range(len(matriz[i])):  # Recorre las columnas
            if matriz[i][j] == objetivo:  # Compara el elemento actual con el objetivo
                return (i, j)  # Devuelve la posición (fila, columna)
    return None  # Si no se encuentra el elemento, devuelve None

# Buscar un elemento
resultado = buscar_elemento(matriz, 6)

if resultado:
    print(f'Elemento encontrado en la posición: {resultado}')  # Salida: Elemento encontrado en la posición: (1, 1)
else:
    print('Elemento no encontrado')