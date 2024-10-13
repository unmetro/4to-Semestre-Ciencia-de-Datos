from functools import reduce


def run(lista):
    # Usar reduce para multiplicar todos los elementos de la lista
    resultado = reduce(lambda x, y: x * y, lista)

    # Imprimir el resultado
    print(resultado)


# llamar a la funcion
run([9, 3, 4, 2])