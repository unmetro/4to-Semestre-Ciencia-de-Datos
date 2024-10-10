def run(values1: list, values2: list) -> list:
    merged = []
    i, j = 0, 0

    while i < len(values1) and j < len(values2):
        if values1[i] < values2[j]:
            if values1[i] not in merged:
                merged.append(values1[i])
            i += 1
        elif values1[i] > values2[j]:
            if values2[j] not in merged:
                merged.append(values2[j])
            j += 1
        else:
            if values1[i] not in merged:
                merged.append(values1[i])
            i += 1
            j += 1

    while i < len(values1):
        if values1[i] not in merged:
            merged.append(values1[i])
        i += 1

    while j < len(values2):
        if values2[j] not in merged:
            merged.append(values2[j])
        j += 1

    return merged

# Llamada de ejemplo
resultado = run([1, 3, 5, 7], [2, 3, 6, 8])
print(resultado)
