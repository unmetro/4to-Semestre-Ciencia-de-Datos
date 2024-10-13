def run(items: list) -> list:
    flatten_items = []
    for elemento in items:
        if isinstance(elemento, list):
            flatten_items.extend(run(elemento))
        else:
            flatten_items.append(elemento)
    return flatten_items

items = [3, [6, [4, 7], 9], 12]
print(run(items))

# # DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)

