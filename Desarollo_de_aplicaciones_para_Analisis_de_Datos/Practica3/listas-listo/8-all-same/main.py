def run(items: list) -> bool:
    for i in items:
        if i != items[0]:
            return False
    return True


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    lista = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(f'La lista {lista},\ntiene todos los elementos iguales: {run(lista)}')  # Output: True
