def run(stock: dict, merch: str, amount: int) -> bool:
    if merch not in stock:
        return False
    if stock[merch] < amount:
        return False
    return True


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    dict1 = {'pen': 20, 'cup': 11, 'keyring': 40}
    print(f'Stock:{dict1} \nArtículo:{'cup'}\nCantidad:{9}\nSalida: {run({'pen': 20, 'cup': 11, 'keyring': 40}, 'cup', 9)}')
