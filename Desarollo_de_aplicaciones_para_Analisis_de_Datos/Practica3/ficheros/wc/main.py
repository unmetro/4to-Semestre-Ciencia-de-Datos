def run(input_path: str) -> tuple:
    try:
        with open(input_path, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        num_lines = len(lineas)
        num_words = sum(len(linea.split()) for linea in lineas)
        num_bytes = sum(len(linea.encode('utf-8')) for linea in lineas)

        return num_lines, num_words, num_bytes
    except FileNotFoundError:
        print(f"LE archivo {input_path} no fue encontrado")

ruta_archivo = 'C:/Users/Bjsan/OneDrive/Escritorio/4semestre/CAAD/Python/ficheros/wc/archivo.txt'
resultado = run(ruta_archivo)

if resultado is not None:
    num_lineas, num_palabras, num_bytes = resultado
    print(f"Número de líneas: {num_lineas}")
    print(f"Número de palabras: {num_palabras}")
    print(f"Número de bytes: {num_bytes}")


# # DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)
