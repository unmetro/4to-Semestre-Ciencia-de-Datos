
def run(to_give_back: float, available_currencies: dict) -> dict | None:
    available_denominations = sorted(available_currencies.keys(), reverse=True)
    money_back = {}

    for currency in available_denominations:
        max_units = available_currencies[currency]  
        count = int(min(to_give_back // currency, max_units))
          
        if count > 0:
            money_back[currency] = count
            to_give_back -= count * currency

        if to_give_back == 0:
            break

    if to_give_back != 0:
        return None

    if not money_back:
        return {}

    return money_back

to_give_back = 7  
available_currencies = {2: 2, 1: 1, 0.5: 8}  
result = run(to_give_back, available_currencies)
print(result)
