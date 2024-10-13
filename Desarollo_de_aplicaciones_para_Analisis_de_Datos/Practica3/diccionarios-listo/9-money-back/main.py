
def run(to_give_back: float, available_currencies: list) -> dict | None:
    available_currencies.sort(reverse=True)
    money_back = {}
    
    for currency in available_currencies:
        count = int(to_give_back // currency)
        if count > 0:
            money_back[currency] = count
            to_give_back -= count * currency
        if to_give_back == 0:
            break

    if to_give_back != 0:
        return None

    return money_back

# Ejemplo de uso
to_give_back = 7
available_currencies = [2, 1, 0.5]
result = run(to_give_back, available_currencies)
print(result)

