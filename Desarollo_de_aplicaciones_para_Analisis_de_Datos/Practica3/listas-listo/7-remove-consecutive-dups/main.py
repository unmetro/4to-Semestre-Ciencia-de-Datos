def run(items: list) -> list:
    if not items:  # Verifica si la items está vacía
        return []
    
    resultado = [items[0]]  # Inicia con el primer elemento de la items
    for i in range(1, len(items)):
        if items[i] != items[i - 1]:  # Solo añade si el elemento actual es diferente al anterior
            resultado.append(items[i])
    
    return resultado

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    list_items = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    print(f'La lista normal:{list_items}\nLa lista sin elementos repetidos:{run(list_items)}')  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
