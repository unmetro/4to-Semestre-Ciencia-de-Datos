def run(items: list, ref_item: object) -> object:
    if ref_item not in items:
        return None

    index = items.index(ref_item)
    if index + 1 < len(items):
        return items[index + 1]
    else:
        return None

# Llamada de ejemplo
resultado = run(['Ana', 'Sara', 'Noelia'], 'Sara')
print(resultado)  # Salida: 'Noelia'
