def run(nums_dups: list) -> list:
    nums_unique = []
    for i in range(len(nums_dups)):
        if nums_dups[i] not in nums_unique:
            nums_unique.append(nums_dups[i])
    return nums_unique


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'La lista: {list1}\nLa lista sin repeticiones: {run(list1)}')  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
