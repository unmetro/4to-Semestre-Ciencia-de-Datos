def run(items: list) -> int | None:
    set_rep = set()
    for i in range(len(items)):
        if items[i] not in set_rep:
            set_rep.add(items[i])
        else:
            fdup = items[i]
            return fdup
    return None

items = [3,2,3,1,5,6,7]
print(f"primer valor repetido: {run(items)}")


# DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)
