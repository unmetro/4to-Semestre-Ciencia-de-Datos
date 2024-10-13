def run(lista):
    # Sumar solo los valores positivos de la lista
    suma_positivos = sum([num for num in lista if num > 0])

    # Imprimir el resultado
    print(suma_positivos)


# llamar a la funcion
run([6, 3, 0, -1, -7, 5])