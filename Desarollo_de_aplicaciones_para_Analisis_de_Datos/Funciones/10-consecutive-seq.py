def consecutive_seq(values, repetitions, index=0, count=1):
    # Caso base: Si llegamos al final de la lista y no encontramos coincidencias
    if index >= len(values) - 1:
        return None

    # Si el elemento actual es igual al siguiente, aumentamos el contador
    if values[index] == values[index + 1]:
        count += 1
    else:
        # Si no son iguales, reiniciamos el contador
        count = 1

    # Si el contador alcanza las repeticiones requeridas, devolvemos el número
    if count == repetitions:
        return values[index]

    # Llamada recursiva al siguiente elemento
    return consecutive_seq(values, repetitions, index + 1, count)


# ejecucion
valores = [1, 74, 56, 56, 56, 332, 8, 8, 8]
repeticiones = 3

resultado = consecutive_seq(valores, repeticiones)
print(f"Resultado: {resultado}")