def run(items: list) -> int:
    lista_enteros = []
    for i in items:
        lista_enteros.append(int(i))
    return sum(lista_enteros)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    lista = [1, '2', 3, '4', 5]
    print(f'La suma de la lista {lista} es: {run(lista)}')
