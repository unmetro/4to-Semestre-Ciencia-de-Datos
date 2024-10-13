def run(values: list) -> int:
    lista_opuesta = [-x for x in values]
    min_value = -max(lista_opuesta)
    return min_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'La lista: {lista}\nEl valor mínimo: {run(lista)}')  # 1
