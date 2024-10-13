import csv
def convertir_valor(valor):
    if valor == '':
        return None
    elif valor == 'True':
        return True
    elif valor == 'False':
        return False
    try:
        return int(valor)
    except ValueError:
        return valor

def run(datafile: str) -> list:
    with open(datafile, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        lista_diccionarios = []
        for fila in lector_csv:
            fila_convertida = {clave: convertir_valor(valor) for clave, valor in fila.items()}
            lista_diccionarios.append(fila_convertida)

        return lista_diccionarios

ruta_csv = 'C:/Users/Bjsan/Downloads/AbandonoEmpleados.csv'
resultado = run(ruta_csv)

for fila in resultado:
    print(fila)

# # DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)
