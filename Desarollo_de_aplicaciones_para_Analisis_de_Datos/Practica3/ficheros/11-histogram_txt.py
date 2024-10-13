def run(fichero_entrada, fichero_salida):
    # Diccionario para almacenar las frecuencias de cada letra
    frecuencias = {}

    # Leer el contenido del fichero de entrada
    with open(fichero_entrada, 'r', encoding='utf-8', errors='ignore') as archivo:
        contenido = archivo.read()

        # Contar la frecuencia de cada letra
        for letra in contenido:
            if letra.isalpha():  # Solo contar letras
                letra = letra.upper()  # Convertir todo a mayúsculas
                if letra in frecuencias:
                    frecuencias[letra] += 1
                else:
                    frecuencias[letra] = 1

    # Crear el fichero de salida con el histograma
    with open(fichero_salida, 'w', encoding='utf-8') as archivo_salida:
        for letra, frecuencia in sorted(frecuencias.items()):
            # Escribir la letra, las barras "■" y el valor de la frecuencia
            archivo_salida.write(f'{letra} {"■" * frecuencia} {frecuencia}\n')


# llamar a la funcion
run('entrada.txt', 'histograma.txt')