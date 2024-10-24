def fibonacci(n: int, a: int, b: int, count: int) -> int:
    a, b = b, a + b  # Actualizar los valores de 'a' y 'b'
    count += 1  # Incrementar el contador

    if count == n + 1:
        return b
    else:
        return fibonacci(n, a, b, count)  # Retornar el valor de la llamada recursiva

count = 2
n = 10
print(f"El valor n-esimo fibonacci es: {fibonacci(n, a=0, b=1, count=count)}")
