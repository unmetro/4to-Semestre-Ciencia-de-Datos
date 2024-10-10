def run(values: list, oper: str) -> bool:
    result = values[0]
    for value in values[1:]:
        if oper == 'and':
            result = result and value
        elif oper == 'or':
            result = result or value
    return result

# Llamada de ejemplo
resultado = run([True, True, False], 'and')
print(resultado)  # Salida: False
