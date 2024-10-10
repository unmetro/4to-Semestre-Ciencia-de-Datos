
def run(input_path: str, line_no: int) -> str | None:
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if 1 <= line_no <= len(lines):
                return lines[line_no - 1].rstrip()
            else:
                return None
    except FileNotFoundError:
        return None

resultado = run("ruta/del/archivo.txt", 3)
print(resultado)
