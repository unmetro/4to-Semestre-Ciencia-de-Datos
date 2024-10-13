def convertir_guion_a_markdown(texto: str) -> str:
    lineas = texto.splitlines()
    markdown = []

    for linea in lineas:
        nivel = 0
        while linea.startswith('\t') or linea.startswith('    '):
            if linea.startswith('\t'):
                nivel += 1
                linea = linea[1:]
            elif linea.startswith('    '):
                nivel += 1
                linea = linea[4:] 

        titulo = linea.strip()
        if titulo:
            encabezado = '#' * (nivel + 1) + ' ' + titulo
            markdown.append(encabezado)
    return '\n'.join(markdown)

def run(input_path: str, output_path: str) -> None:
    with open(input_path, 'r', encoding='utf-8') as f:
        texto = f.read()

    markdown = convertir_guion_a_markdown(texto)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown)

input_path = 'C:/Users/Bjsan/OneDrive/Escritorio/4semestre/CAAD/Python/ficheros/txt2md/prueba.txt'
output_path = 'C:/Users/Bjsan/OneDrive/Escritorio/4semestre/CAAD/Python/ficheros/txt2md/guion.txt'

run(input_path, output_path)
