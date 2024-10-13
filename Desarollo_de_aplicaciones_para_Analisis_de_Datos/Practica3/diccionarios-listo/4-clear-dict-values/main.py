def run(items: dict) -> dict:

    diccionario_vacio = {clave: [] for clave, valor in diccionario_original.items()}

    return diccionario_vacio


diccionario_original = {'A': [0, 1], 'B': [2, 3], 'C': [4, 5]}
print(run(diccionario_original))

# # DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)
