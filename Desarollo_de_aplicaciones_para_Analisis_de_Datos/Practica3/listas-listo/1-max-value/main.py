def run(values: list) -> int:
    max_value = values[0]
    for i in range(0, len(values)):
        if i == len(values) - 1:
            break
        if max_value >= values[i + 1]:
            pass
        else:
            max_value = values[i + 1]
    return max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(f'La lista:{lista}\nSu elemento máximo:{run(lista)}')  # 5