def run(items: dict) -> bool:
    first_value = items.get('a')
    for valor in items.values():
        if valor != first_value:
            return False
    return True

diccionario = {'a':1,'b':2,'c':1}
print(f"El diccionario tiene los mismos valores? {run(diccionario)}")

# # DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)
