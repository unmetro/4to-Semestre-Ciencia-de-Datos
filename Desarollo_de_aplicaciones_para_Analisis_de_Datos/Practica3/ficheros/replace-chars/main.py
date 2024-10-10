

def run(input_path: str, replacements: str, output_path: str) -> None:
    replacement_dict = {pair[0]: pair[1] for pair in replacements.split('|')}
    try:
        with open(input_path, 'r', encoding='utf-8') as infile:
            content = infile.read()
        for old_char, new_char in replacement_dict.items():
            content = content.replace(old_char, new_char)
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
    except FileNotFoundError:
        print(f"El archivo {input_path} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

run('entrada.txt', 'aA|bB|cC', 'salida.txt')
