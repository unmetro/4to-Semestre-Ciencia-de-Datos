#print("Desarollo de aplicaciones para Anilisis de Datos")

import multiprocessing
import random

# 1. Crear un algoritmo para sumar dos vectores
def sumar_vectores(vector1, vector2):
    return [vector1[i] + vector2[i] for i in range(len(vector1))]

# Crear una función que sume dos números (para evitar problemas de serialización)
def suma_elementos(x, y):
    return x + y

# 2. Crear una función para realizar la suma en paralelo
def sumar_vectores_paralelo(vector1, vector2):
    with multiprocessing.Pool() as pool:
        result = pool.starmap(suma_elementos, zip(vector1, vector2))
    return result

# 3. Generar dos vectores con valores aleatorios
tamaño_vector = 1000  # Tamaño del vector
vector1 = [random.randint(1, 100) for _ in range(tamaño_vector)]
vector2 = [random.randint(1, 100) for _ in range(tamaño_vector)]

# 4. Sumar los vectores de forma secuencial y paralela
resultado_secuencial = sumar_vectores(vector1, vector2)
resultado_paralelo = sumar_vectores_paralelo(vector1, vector2)

# 5. Mostrar los resultados
print(f"Resultado Secuencial: {resultado_secuencial[:10]}...")  # Mostramos los primeros 10 elementos para verificar
print(f"Resultado Paralelo: {resultado_paralelo[:10]}...")  # Mostramos los primeros 10 elementos para verificar

# Comparar resultados
if resultado_secuencial == resultado_paralelo:
    print("Los resultados son iguales")
else:
    print("Los resultados son diferentes")

