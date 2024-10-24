def bsort(input_list):
    # copia de lista original
    lst = input_list[:]
    n = len(lst)

    # Implementamos el algoritmo de burbuja
    for i in range(n):
        # En cada pasada, los elementos más grandes se mueven hacia el final
        for j in range(0, n - i - 1):
            # Intercambiamos si el elemento actual es mayor que el siguiente
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


    return lst


# ejecucion
lista = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = bsort(lista)

print(f"Lista original: {lista}")
print(f"Lista ordenada: {lista_ordenada}")