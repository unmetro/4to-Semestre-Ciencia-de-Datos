def run(nombre_completo):
    # Separar el nombre completo en apellido y nombre usando la coma
    apellido, nombre = nombre_completo.split(", ")

    # Obtener las iniciales del nombre (solo la primera letra) y del apellido
    iniciales_nombre = nombre[0].upper() + '.'
    iniciales_apellido = ''.join([palabra[0].upper() + '.' for palabra in apellido.split()])

    # Combinar las iniciales del nombre y del apellido
    iniciales = iniciales_nombre + iniciales_apellido

    print(iniciales)


# llamar a la funcion
run('van Rossum, Guido')