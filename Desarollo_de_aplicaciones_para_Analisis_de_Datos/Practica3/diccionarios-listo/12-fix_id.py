def run(lista_registros):
    # Nueva lista para almacenar los registros con los IDs corregidos
    nueva_lista = []

    # Iterar sobre la lista de registros y asignar un ID secuencial
    for i, registro in enumerate(lista_registros, start=1):
        nuevo_registro = registro.copy()  # Copiar el registro para no modificar el original
        nuevo_registro['id'] = i  # Asignar el nuevo ID secuencial
        nueva_lista.append(nuevo_registro)

    # Imprimir la nueva lista con los ID corregidos
    return nueva_lista


# llamar a la funcion
lista_registros = [
    {'id': 1, 'codename': 'Jessie', 'released_at': 2015},
    {'id': 3, 'codename': 'Stretch', 'released_at': 2017},
    {'id': 5, 'codename': 'Buster', 'released_at': 2019},
    {'id': 6, 'codename': 'Bullseye', 'released_at': 2021},
    {'id': 7, 'codename': 'Bookworm', 'released_at': 2023}
]

nueva_lista = run(lista_registros)
print(nueva_lista)