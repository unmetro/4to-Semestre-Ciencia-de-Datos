class IntegerStackIterator:
    def __init__(self, stack: 'IntegerStack'):
        """Inicializa el iterador con la pila dada."""
        self._stack = stack
        self._index = len(stack.items) - 1  # Empieza desde el top de la pila

    def __next__(self) -> int:
        """Retorna el siguiente elemento en la pila."""
        if self._index >= 0:
            value = self._stack.items[self._index]
            self._index -= 1  # Mueve el índice hacia abajo en la pila
            return value
        else:
            raise StopIteration  # No hay más elementos para iterar

# Para hacer que la clase IntegerStack sea iterable, añadimos el método __iter__:
class IntegerStack:
    def __init__(self, *, max_size: int = 10):
        self.items = []
        self.max_size = max_size

    def push(self, item: int) -> bool:
        if len(self.items) < self.max_size:
            self.items.append(item)
            return True
        else:
            return False

    def pop(self) -> int:
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self) -> int:
        if self.items:
            return self.items[-1]
        else:
            return None

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def is_full(self) -> bool:
        return len(self.items) == self.max_size

    def size(self) -> int:
        return len(self.items)

    def __iter__(self):
        """Devuelve un iterador para la pila."""
        return IntegerStackIterator(self)

# Ejemplo de uso:
stack = IntegerStack(max_size=5)
stack.push(3)
stack.push(7)
stack.push(1)
stack.push(6)
stack.push(2)

# Ahora podemos iterar sobre la pila con un bucle for
for item in stack:
    print(item)  # Imprimirá los elementos de la pila desde el top hacia el fondo
