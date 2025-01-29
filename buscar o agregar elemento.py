# Función para buscar un elemento en la matriz y agregarlo si no se encuentra

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

def buscar_y_agregar_elemento(matriz, objetivo):
    # Buscar el elemento
    for i in range(len(matriz)):  # Recorre las filas
        for j in range(len(matriz[i])):  # Recorre las columnas
            if matriz[i][j] == objetivo:  # Compara el elemento actual con el objetivo
                return (i, j)  # Devuelve la posición (fila, columna)
    
    # Si no se encuentra el elemento, se agrega a una nueva fila
    nueva_fila = [objetivo]  # Crear una nueva fila con el elemento
    matriz += [nueva_fila]  # Concatenar la nueva fila a la matriz

    return None  # Devuelve None si el elemento fue agregado

# Matriz de ejemplo
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Elemento a buscar
objetivo = 99

# Buscar y agregar el elemento
resultado = buscar_y_agregar_elemento(matriz, objetivo)

if resultado:
    print(f'Elemento encontrado en la posición: {resultado}')  # Salida: Elemento encontrado en la posición: (fila, columna)
else:
    print(f'Elemento {objetivo} no encontrado. Ha sido agregado a la matriz.')

# Imprimir la matriz resultante
print(matriz)