

def run(input_path: str, lower_bound: int) -> dict:
    freq = {}
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read().lower().split()
            for word in content:
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1
        freq = {word: count for word, count in freq.items() if count >= lower_bound}
        return freq
    except FileNotFoundError:
        print(f"El archivo {input_path} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {}

# Llamada a la función con un archivo de ejemplo y un valor umbral
resultado = run("ruta_del_archivo.txt", 2)
print(resultado)
