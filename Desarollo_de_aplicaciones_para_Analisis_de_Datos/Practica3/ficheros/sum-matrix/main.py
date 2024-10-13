def run(matrix1_path: str, matrix2_path: str, result_path: str) -> None:
    """Lee dos matrices desde archivos, las suma y escribe el resultado en un archivo de salida."""
    
    # Leer las dos matrices desde los archivos
    with open(matrix1_path, 'r') as archivo1, open(matrix2_path, 'r') as archivo2:
        matriz1 = [list(map(int, linea.split())) for linea in archivo1]
        matriz2 = [list(map(int, linea.split())) for linea in archivo2]
    
    # Sumar las matrices
    matriz_resultado = []
    for fila1, fila2 in zip(matriz1, matriz2):
        fila_resultado = [x + y for x, y in zip(fila1, fila2)]
        matriz_resultado.append(fila_resultado)
    
    # Escribir la matriz resultante en el archivo de salida
    with open(result_path, 'w') as archivo_salida:
        for fila in matriz_resultado:
            archivo_salida.write(' '.join(map(str, fila)) + '\n')

    print(f"La suma de las matrices se ha guardado en {result_path}")

# Ejemplo de uso
matrix1_path = 'matriz1.txt'  # Cambia esto por la ruta de tu archivo de la primera matriz
matrix2_path = 'matriz2.txt'  # Cambia esto por la ruta de tu archivo de la segunda matriz
result_path = 'resultado.txt'  # Archivo de salida

# Llamar a la función con los archivos correspondientes
run(matrix1_path, matrix2_path, result_path)
