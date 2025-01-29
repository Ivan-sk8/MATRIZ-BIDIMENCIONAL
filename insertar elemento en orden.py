# Función para insertar un elemento en orden
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

def insertar_en_orden(matriz, elemento):
    # Buscar la fila donde se debe insertar el elemento
    for i in range(len(matriz)):
        if matriz[i] and matriz[i][-1] >= elemento:  # Si la fila no está vacía y el último elemento es mayor o igual
            # Insertar el elemento en la posición correcta dentro de la fila
            matriz[i] += [elemento]  # Agregar el elemento al final de la fila
            matriz[i].sort()  # Ordenar la fila
            return

    # Si no se encontró una fila adecuada, agregar una nueva fila
    matriz += [[elemento]]  # Crear una nueva fila con el elemento


# Matriz de ejemplo
matriz = [[1, 2, 3], [4, 6], [7, 8, 9]]

# Elemento a insertar
nuevo_elemento = 11

# Insertar el elemento en orden
insertar_en_orden(matriz, nuevo_elemento)

# Imprimir la matriz resultante
print(matriz)