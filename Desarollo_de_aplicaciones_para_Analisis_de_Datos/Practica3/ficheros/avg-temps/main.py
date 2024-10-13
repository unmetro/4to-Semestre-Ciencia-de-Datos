def leer_temperaturas(input_path: str) -> list:
    with open(input_path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
    temperaturas_por_mes = []

    for linea in lineas:
        temperaturas = list(map(float, linea.strip().split(',')))
        temperaturas_por_mes.append(temperaturas)

    return temperaturas_por_mes

def calcular_media_mensual(temperaturas_por_mes: list) -> list:
    medias_mensuales = []

    for temperaturas in temperaturas_por_mes:
        media = sum(temperaturas) / len(temperaturas)
        medias_mensuales.append(media)

    return medias_mensuales

def escribir_medias(medias_mensuales: list, output_path: str) -> None:
    with open(output_path, 'w', encoding='utf-8') as f:
        for media in medias_mensuales:
            f.write(f"{media:.2f}\n")

def run(input_path: str, output_path: str) -> None:
    temperaturas_por_mes = leer_temperaturas(input_path)
    medias_mensuales = calcular_media_mensual(temperaturas_por_mes)
    escribir_medias(medias_mensuales, output_path)

input_path = 'C:/Users/Bjsan/OneDrive/Escritorio/4semestre/CAAD/Python/ficheros/avg-temps/prueba.csv'
output_path = 'C:/Users/Bjsan/OneDrive/Escritorio/4semestre/CAAD/Python/ficheros/avg-temps/fichero_salida.txt'
run(input_path, output_path)
