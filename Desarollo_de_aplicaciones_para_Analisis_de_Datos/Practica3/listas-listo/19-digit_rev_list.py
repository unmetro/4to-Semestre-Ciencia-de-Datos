def run(numero):
    # Convertir el número a una cadena, invertirlo, luego volver a convertir cada carácter a entero
    resultado = [int(digito) for digito in str(numero)[::-1]]

    # Imprimir el resultado
    print(resultado)


# llamar a la funcion
run(56442)