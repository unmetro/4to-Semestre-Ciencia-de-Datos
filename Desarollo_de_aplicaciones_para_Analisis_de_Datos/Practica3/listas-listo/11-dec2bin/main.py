def run(n: int) -> str:
    bin_repr = ''
    if n == 0:
        return '0'
    while n > 0:
        bin_repr = str(n % 2) + bin_repr
        n = n // 2
    return bin_repr


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    num_decimal = 56
    print(f'Numero decimal:{num_decimal}\n Binario: {run(num_decimal)}')
