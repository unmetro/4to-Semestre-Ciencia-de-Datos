def run(values: list) -> list:
    return [num for num in values if num % 2 != 0]

# Llamada de ejemplo
resultado = run([7, 3, 4, 8, 12, 6, 9])
print(resultado)  # Salida: [7, 3, 9]
