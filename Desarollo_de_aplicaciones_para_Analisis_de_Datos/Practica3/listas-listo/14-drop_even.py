def run(lista):
    # Usar comprensión de listas para seleccionar elementos en posiciones impares
    resultado = [lista[i] for i in range(len(lista)) if i % 2 != 0]

    # Imprimir el resultado
    print(f'La lista eliminando los elementos en posiciones pares es: {resultado}')


# llamar a la funcion
run(['U', 'V', 'W', 'X', 'Y'])