import re
from collections import Counter
def run(input_path: str) -> str:
    """Encuentra la palabra más larga en un fichero de texto, considerando caracteres especiales."""
    
    # Definir los caracteres frontera de palabras que se deben eliminar: . , ; : ( )
    frontera = r"[.,;:()']"

    # Leer el contenido del archivo
    with open(input_path, 'r') as archivo:
        contenido = archivo.read()

    # Eliminar los caracteres especiales definidos en 'frontera'
    contenido_limpio = re.sub(frontera, '', contenido)

    # Dividir el texto en palabras
    palabras = contenido_limpio.split()

    # Crear un diccionario para contar las frecuencias de las palabras
    frecuencias = {}
    
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    # Filtrar solo las palabras más largas
    max_longitud = max(len(palabra) for palabra in palabras)
    palabras_mas_largas = [palabra for palabra in palabras if len(palabra) == max_longitud]

    # Elegir la palabra más frecuente entre las palabras más largas
    palabra_mas_larga = palabras_mas_largas[0]  # Inicializar con la primera palabra más larga
    max_frecuencia = frecuencias[palabra_mas_larga]  # Frecuencia de la primera palabra

    for palabra in palabras_mas_largas:
        if frecuencias[palabra] > max_frecuencia:
            palabra_mas_larga = palabra
            max_frecuencia = frecuencias[palabra]

    return palabra_mas_larga

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    input_path = 'texto.txt'
    resultado = run('java.txt')
    print(f"La palabra más larga es: {resultado}")