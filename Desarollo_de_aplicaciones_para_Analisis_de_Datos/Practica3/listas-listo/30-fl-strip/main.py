def run(numbers: str) -> str:
    elements = numbers.split(',')
    if len(elements) <= 2:
        return ''
    strip_numbers = ' '.join(elements[1:-1])
    return strip_numbers

# Llamada de ejemplo
resultado = run('1,2,3,4,5')
print(resultado)  # Salida: '2 3 4'
