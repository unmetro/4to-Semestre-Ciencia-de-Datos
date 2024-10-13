import re 
def run(fichero, palabra_objetivo):
    ocurrencias = []
    palabra_objetivo = palabra_objetivo.lower()  # Para hacer que la búsqueda no distinga entre mayúsculas y minúsculas

    with open('help.txt', 'r') as archivo:
        for num_linea, linea in enumerate(archivo, 1):  # Enumerar las líneas, empezando por 1
            palabras = re.finditer(r'\b' + re.escape(palabra_objetivo) + r'\b', linea, re.IGNORECASE)
            for match in palabras:
                # Guardar la tupla (número de línea, índice de columna)
                ocurrencias.append((num_linea, match.start() + 1))

    return ocurrencias

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(run("data.txt", "you"))