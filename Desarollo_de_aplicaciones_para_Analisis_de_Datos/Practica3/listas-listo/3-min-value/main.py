def run(values: list) -> int:
    min_value = values[0]
    for i in range(0, len(values)):
        if i == len(values) - 1:
            break
        if min_value <= values[i + 1]:
            pass
        else:
            min_value = values[i + 1]
    return min_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(f'La lista:{lista}\nSu elemento mínimo:{run(lista)}')  # 1
