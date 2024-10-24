def count_vowels(text):
    # Lista de vocales incluyendo las con tilde
    vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ"

    # Caso base: Si la cadena está vacía, no hay más vocales
    if text == "":
        return 0

    # Si el primer carácter es una vocal, sumamos 1 y seguimos con el resto de la cadena
    if text[0] in vowels:
        return 1 + count_vowels(text[1:])

    # Si no es una vocal, seguimos con el resto de la cadena sin sumar
    else:
        return count_vowels(text[1:])


#ejecucion
texto = "Ayer empecé a programar"
resultado = count_vowels(texto)
print(f"El texto '{texto}' tiene {resultado} vocales.")