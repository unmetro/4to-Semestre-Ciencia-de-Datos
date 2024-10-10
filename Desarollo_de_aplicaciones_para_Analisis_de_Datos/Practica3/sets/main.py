def run(number: str) -> bool:
    number_set = {1,0}
    for c in number:
        if int(c) not in number_set:
            return False
    return True

number = input("introduzca un numero binario: ")
print(f"Es numero es binario?: {run(number)}")