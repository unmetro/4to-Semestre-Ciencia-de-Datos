
def run(text: str) -> str:
    list_cadena = text.split()
    reversing = list_cadena[::-1]
    return ' '.join(reversing)

text = 'Hola como estan'
print(run(text))

# # DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)
