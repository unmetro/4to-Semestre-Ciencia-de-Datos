import string

def is_pangram(text):
    # Convertimos el texto a minúsculas para evitar diferencias de mayúsculas/minúsculas
    text = text.lower()

    # Eliminamos espacios y caracteres no alfabéticos
    text = ''.join(char for char in text if char.isalpha())

    # Creamos un conjunto con todas las letras del abecedario
    alphabet = set(string.ascii_lowercase)

    # Comparamos si el conjunto del alfabeto está contenido en el texto dado
    return alphabet.issubset(set(text))


# ejecucion
frase1 = "Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol"
frase2 = "No utilizo todas las letras del abecedario"

print(f"¿La frase 1 es pangrama? {is_pangram(frase1)}")
print(f"¿La frase 2 es pangrama? {is_pangram(frase2)}")