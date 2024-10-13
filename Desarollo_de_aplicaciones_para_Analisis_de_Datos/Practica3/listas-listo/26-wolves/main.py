def run(farm: list) -> str:
    wolf_index = farm.index('lobo')
    if wolf_index == len(farm) - 1:
        return "Oye lobo no te quiero ver más por aquí"
    else:
        sheep_index = len(farm) - wolf_index - 1
        return f"Cuidado oveja {sheep_index}, el lobo te va a comer"

# Llamada de ejemplo
resultado1 = run(['oveja', 'oveja', 'lobo', 'oveja'])
print(resultado1)  # Salida: Cuidado oveja 1, el lobo te va a comer

resultado2 = run(['oveja', 'oveja', 'oveja', 'lobo'])
print(resultado2)  # Salida: Oye lobo no te quiero ver más por aquí
