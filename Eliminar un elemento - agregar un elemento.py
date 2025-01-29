# Función para eliminar un elemento específico

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]


def eliminar_elemento(matriz, objetivo):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == objetivo:
                del matriz[i][j]  # Eliminar el elemento en la posición (i, j)
                return
    print("Elemento no encontrado")

eliminar_elemento(matriz, 5)

print(matriz)  # Salida: [[1, 2, 3], [4, 6], [7, 8, 9]]

#agregar un elemento a una matriz bidimensional

matriz[1] = matriz[1][:1] + [5] + matriz[1][1:]

print(matriz)