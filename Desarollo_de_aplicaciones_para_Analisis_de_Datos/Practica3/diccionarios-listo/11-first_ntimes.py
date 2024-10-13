def run(lista, n):
    # Crear un diccionario para contar las ocurrencias de cada número
    ocurrencias = {}

    # Contar las ocurrencias de cada número
    for num in lista:
        if num in ocurrencias:
            ocurrencias[num] += 1
        else:
            ocurrencias[num] = 1

    # Buscar el primer número en la lista original que tenga exactamente n ocurrencias
    for num in lista:
        if ocurrencias[num] == n:
            return num

    # Si no se encuentra ningún número que se repita exactamente n veces
    return -1


# llamar a la funcion
print(run([2, 3, 5, 3, 2, 1, 8, 2], 3))