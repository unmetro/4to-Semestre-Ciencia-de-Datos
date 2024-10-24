def hyperfactorial(n: int, sum: int) -> int:
    if n == 0:
        return sum
    else:
        h_factorial = pow(n, n)
        sum += h_factorial
        return hyperfactorial(n - 1, sum)

n = 5
sum = 0
print(f"El hiperfactorial de {n} es: {hyperfactorial(n, sum)}")


# El hiperfactorial de un numero n se calcula como el producto sucesivo de los decrementos de
# n elevado a sı mismo. Escribe una funci´on que calcule el hiperfactorial de un numero.