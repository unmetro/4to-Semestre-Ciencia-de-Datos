def run(lista):
    # Obtener la suma de los valores opuestos (negativos de los valores de la lista)
    suma_opuestos = sum([-num for num in lista])

    # Imprimir el resultado
    print(suma_opuestos)


# llamar a la funcion
run([6, 3, 0, -1, -7, 5])