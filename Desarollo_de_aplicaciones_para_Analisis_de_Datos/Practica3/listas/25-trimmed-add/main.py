def run(values: list) -> int:
    if len(values) < 3:
        return 0
    return sum(values) - max(values) - min(values)

# Llamada de ejemplo
resultado = run([7, 12, 4, 9, 3])
print(resultado)
