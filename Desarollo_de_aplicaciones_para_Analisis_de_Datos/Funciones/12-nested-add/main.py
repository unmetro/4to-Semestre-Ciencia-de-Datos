def add(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):  # Si el elemento es una lista, llama a la función recursivamente
            total += add(element)
        else:
            total += element  # Si es un número, lo suma al total
    return total

lst = [1, [2, 4], 5, [6, [7, 8]]]
print(f"Suma de la lista: {add(lst)}")

#Regresa la suma total de una lista que puede tener listas anidadas a traves de una funicon recursiva