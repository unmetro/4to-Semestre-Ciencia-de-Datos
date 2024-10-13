def run(x, n):
    # Generar lista de múltiplos usando comprensión de listas
    multiplos = [x * i for i in range(1, n + 1)]

    # Imprimir el resultado
    print(f'Los primeros {n} múltiplos de {x} son: {multiplos}')


# Llamar a la funcion
run(2, 4)