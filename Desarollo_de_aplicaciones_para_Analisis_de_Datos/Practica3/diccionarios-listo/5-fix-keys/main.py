def run(items: dict) -> dict:
    fitems = {}
    key_values = list(items.keys())
    for i in range(len(key_values)):
        key_values[i] = key_values[i].replace(" ", "")
    for i in range(len(key_values)):
        fitems[key_values[i]] = items[list(items.keys())[i]] 
    return fitems


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(run({"key 1": "value 1", "key 2": "value 2"}))  # Expected output: {'key1': 'value 1', 'key2': 'value 2'}
