def run(n: int) -> list:
    lista = [2 ** i for i in range(n+1)]
    return lista


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    list_items = 10
    print(f'La lista de potencias de 2 hasta {list_items} es:\n{run(list_items)}')  # Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
