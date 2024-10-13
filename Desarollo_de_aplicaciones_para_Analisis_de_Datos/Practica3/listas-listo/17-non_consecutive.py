def run(lista):
    # Recorrer la lista a partir del segundo elemento
    for i in range(1, len(lista)):
        # Si la diferencia entre el valor actual y el anterior no es 1, no son consecutivos
        if lista[i] != lista[i - 1] + 1:
            return lista[i]  # Retornar el primer número no consecutivo
    return None  # Si todos los números son consecutivos

# llamar a la funcion
print(run([1, 2, 4, 5]))  # Debe retornar 4
print(run([1, 2, 3, 4]))  # Debe retornar None