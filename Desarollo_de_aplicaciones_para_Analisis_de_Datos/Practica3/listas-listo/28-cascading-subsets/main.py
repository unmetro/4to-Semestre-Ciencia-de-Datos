def run(values: list, size: int) -> list:
    cascading = [tuple(values[i:i+size]) for i in range(len(values) - size + 1)]
    return cascading

# Llamada de ejemplo
resultado = run([1, 2, 3, 4], 2)
print(resultado)  # Salida: [(1, 2), (2, 3), (3, 4)]
