def run(formula: list) -> bool:
    # Regla 1: El componente 1 y el componente 2 no pueden estar juntos.
    if 1 in formula and 2 in formula:
        return False

    # Regla 2: El componente 3 y el componente 4 no pueden estar juntos.
    if 3 in formula and 4 in formula:
        return False

    # Regla 3: El componente 5 y el componente 6 deben estar ambos o ninguno.
    if (5 in formula and 6 not in formula) or (6 in formula and 5 not in formula):
        return False

    # Regla 4: Al menos uno de los componentes 7 u 8 debe estar presente.
    if 7 not in formula and 8 not in formula:
        return False

    return True

# Llamada de ejemplo
resultado = run([1, 3, 5, 6, 8])
print(resultado)  # Salida: True
