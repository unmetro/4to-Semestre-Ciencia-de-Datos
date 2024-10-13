def run(items: list) -> dict:
    salida = {sublista[0]: sublista[1:] for sublista in items}
    return salida

lista = [['Item1', 'A', 'B','i'], ['Item2', 'C', 'D','f'], ['Item3', 'E', 'F','t']]
print(run(lista))

# # DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)
