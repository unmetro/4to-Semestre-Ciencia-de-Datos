def run(lista, n):
    # Verificar si el índice está dentro del rango de la lista
    if n < 0 or n >= len(lista):
        return -1  # Retornar -1 si n está fuera de rango
    else:
        # Calcular el valor del elemento en la posición n elevado a n
        return lista[n] ** n

# llamar a la funcion
print(run([6, 3, 8, 4], 2))