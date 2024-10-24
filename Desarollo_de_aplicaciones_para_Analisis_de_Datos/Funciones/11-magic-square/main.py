def is_magic_square(matrix):
    # Obtener la suma de la primera fila como referencia
    n = len(matrix)
    sum_ref = sum(matrix[0])

    # Comprobar las sumas de las filas
    for row in matrix:
        if sum(row) != sum_ref:
            return False

    # Comprobar las sumas de las columnas
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != sum_ref:
            return False

    # Comprobar la suma de la diagonal principal
    if sum(matrix[i][i] for i in range(n)) != sum_ref:
        return False

    # Comprobar la suma de la diagonal secundaria
    if sum(matrix[i][n - i - 1] for i in range(n)) != sum_ref:
        return False

    return True

# Ejemplo de uso:
matrix = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

print(is_magic_square(matrix))


# Escribe una función que, dada una lista de listas (como matriz cuadrada), determina si es o
# no un cuadrado mágico. Esto a través de la suma de columnas, filas y diagonal
