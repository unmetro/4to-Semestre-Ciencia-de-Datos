from itertools import combinations


def run(fichero_entrada, fichero_salida):
    # Leer todas las líneas del fichero de entrada
    with open(fichero_entrada, 'r', encoding='utf-8') as archivo:
        lineas = [line.strip().lower() for line in archivo.readlines()]  # Convertir a minúsculas

    # Abrir el fichero de salida para escribir los resultados
    with open(fichero_salida, 'w', encoding='utf-8') as archivo_salida:
        # Generar todas las combinaciones posibles de dos líneas
        for (i, linea_a), (j, linea_b) in combinations(enumerate(lineas), 2):
            # Dividir ambas líneas en palabras
            palabras_a = set(linea_a.split())
            palabras_b = set(linea_b.split())

            # Encontrar palabras comunes
            comunes = palabras_a & palabras_b  # Intersección de conjuntos

            # Escribir el número de palabras comunes en el fichero de salida
            archivo_salida.write(f'{len(comunes)}\n')


# llamar a la funcion
run('entrada_palabras.txt', 'salida_palabras.txt')