def run(fichero_entrada):
    # Inicializar variables
    distancia = 0
    profundidad = 0
    with open(fichero_entrada, 'r') as archivo:
        # Leer la primera línea para obtener los litros de combustible
        combustible = int(archivo.readline().strip())

        # Leer los movimientos del submarino
        movimientos = archivo.readline().strip().split(',')

    # Procesar cada movimiento
    for movimiento in movimientos:
        # Separar distancia y cambio de profundidad
        x, y = map(int, movimiento.split(':'))

        # Actualizar la distancia y la profundidad
        nueva_distancia = distancia + x
        nueva_profundidad = profundidad + y

        # Validar límites de profundidad
        if nueva_profundidad < 0:
            nueva_profundidad = 0  # No puede ascender por encima de la superficie
        if nueva_profundidad > 600:
            nueva_profundidad = 600  # No puede descender por debajo de 600

        # Calcular consumo de combustible
        consumo = 3 * x + 2 * abs(y)
        if combustible < consumo:
            break  # Si no hay suficiente combustible, se detiene el submarino

        # Actualizar los valores si todo es válido
        distancia = nueva_distancia
        profundidad = nueva_profundidad
        combustible -= consumo

    # Imprimir resultados
    print(f'Distancia: {distancia}')
    print(f'Profundidad: {profundidad}')
    print(f'Combustible restante: {combustible}')


# llamar a la funcion
run('entrada_submarino.txt')