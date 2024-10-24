import string


def cycle_alphabet(num_chars):
    # Obtenemos el alfabeto en minúsculas
    alphabet = string.ascii_lowercase
    alphabet_length = len(alphabet)

    # Generamos caracteres de forma cíclica
    for i in range(num_chars):
        yield alphabet[i % alphabet_length]


# ejecucion
num_chars_10 = 10
resultado_10 = ''.join(cycle_alphabet(num_chars_10))
print(f"Con num_chars= {num_chars_10} : {resultado_10}")

num_chars_43 = 43
resultado_43 = ''.join(cycle_alphabet(num_chars_43))
print(f"Con num_chars= {num_chars_43} : {resultado_43}")