from functools import wraps

def assert_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Verificar si todos los argumentos numéricos son positivos
        for arg in list(args) + list(kwargs.values()):
            if isinstance(arg, (int, float)) and arg <= 0:
                return None  # Si algún argumento no es positivo, devolver None
        # Si todos los argumentos numéricos son positivos, ejecutar la función
        return func(*args, **kwargs)
    return wrapper

# Ejemplo de uso
@assert_positive
def add(x, y):
    return x + y

print(add(2, 3))    # Debería imprimir: 5
print(add(-2, 3))   # Debería imprimir: None
