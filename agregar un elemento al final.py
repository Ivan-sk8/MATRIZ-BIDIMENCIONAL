# Matriz original
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

# Nuevo dato que quieres agregar como una nueva fila
nuevo_dato = 7

# Crear una nueva matriz con una fila adicional
nueva_matriz = [[0] * len(matriz[0]) for _ in range(len(matriz) + 1)]

# Copiar las filas existentes
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        nueva_matriz[i][j] = matriz[i][j]

# Agregar el nuevo dato como una nueva fila
nueva_matriz[-1] = [nuevo_dato]  # Crear una nueva fila con el nuevo dato

print(nueva_matriz)