
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Ejemplo de uso
n = 10
resultado = list(fibonacci(n))
print(resultado)
