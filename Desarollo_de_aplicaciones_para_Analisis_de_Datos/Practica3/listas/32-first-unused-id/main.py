def run(ids: list) -> int:
    ids_set = set(ids)
    first_unused_id = 1
    while first_unused_id in ids_set:
        first_unused_id += 1
    return first_unused_id

# Llamada de ejemplo
resultado = run([3, 1, 8, 4, 9])
print(resultado)  # Salida: 2
