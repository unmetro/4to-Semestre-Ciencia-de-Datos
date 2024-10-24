
def is_palindrome(text):
    # Limpiamos el texto: eliminamos espacios y convertimos a minúsculas
    text = ''.join(text.split()).lower()

    # Caso base: Si la longitud del texto es 0 o 1, es un palíndromo
    if len(text) <= 1:
        return True

    # Verificamos si el primer y último carácter coinciden
    if text[0] == text[-1]:
        # Llamada recursiva con el texto sin el primer y último carácter
        return is_palindrome(text[1:-1])
    else:
        # Si no coinciden, no es un palíndromo
        return False

# Ejemplos de uso
print(is_palindrome("Mom"))  # Debería imprimir: True
print(is_palindrome("Son"))  # Debería imprimir: False
