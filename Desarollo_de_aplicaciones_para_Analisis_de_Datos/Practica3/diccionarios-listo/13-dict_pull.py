def run(diccionario, claves):
    # Crear un nuevo diccionario utilizando diccionarios por comprensión
    nuevo_diccionario = {clave: diccionario[clave] for clave in claves if clave in diccionario}

    # Imprimir el resultado
    return nuevo_diccionario


# llamar a la funcion
diccionario = {'math': 9.75, 'biology': 6.83, 'art': 5.42, 'english': 7.50}
claves = ('biology', 'art')

resultado = run(diccionario, claves)
print(resultado)