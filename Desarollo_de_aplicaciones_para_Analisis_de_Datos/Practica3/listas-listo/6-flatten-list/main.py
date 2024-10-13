def run(items: list) -> list:
    flatten_items = []
    for i in items:
        if type(i) == list:
            for j in i:
                flatten_items.append(j)
        else:
            flatten_items.append(i)
    return flatten_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    list1 = [1, 2, [3, 4, 5], 6, 7, [8, 9], 10]
    print(f'La lista: {list1}\nLa lista aplanada: {run(list1)}')  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
