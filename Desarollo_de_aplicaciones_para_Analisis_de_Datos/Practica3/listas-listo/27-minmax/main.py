def run(values: list) -> tuple:
    if not values:
        return None, None

    min_value = values[0]
    max_value = values[0]

    for value in values[1:]:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value

    return min_value, max_value

# Llamada de ejemplo
resultado = run([4, 2, 8, 11, 23, 8, 9])
print(f"min = {resultado[0]} y max = {resultado[1]}")
