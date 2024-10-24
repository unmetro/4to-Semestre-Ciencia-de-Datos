
def rslice(text, size):
    # Caso base: Si la cadena está vacía, devolver una lista vacía
    if not text:
        return []

    # Dividir el texto en el primer trozo y el resto
    return [text[:size]] + rslice(text[size:], size)

# Ejemplo de uso
texto = 'Ahora es mejor que nunca'
tamaño = 4
resultado = rslice(texto, tamaño)
print(resultado)
