def run(values: list) -> int:
    numeros_opuestos=[-x for x in values]
    max_value = -min(numeros_opuestos)
    return max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5] 
    print(f'La lista:{lista}\nSu elemento máximo:{run(lista)}')  # 5