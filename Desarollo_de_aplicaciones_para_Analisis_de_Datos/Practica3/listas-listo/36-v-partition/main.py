def run(values: list, ref_value: int) -> list:
    less_than = [x for x in values if x < ref_value]
    greater_or_equal = [x for x in values if x >= ref_value]
    return [less_than, greater_or_equal]

# Llamada de ejemplo
resultado = run([4, 3, 2, 9, 8, 5], 4)
print(resultado)  # Salida: [[3, 2], [4, 9, 8, 5]]
