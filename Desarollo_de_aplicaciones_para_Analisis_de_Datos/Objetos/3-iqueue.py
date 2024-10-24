class IntegerQueue:
    def __init__(self, *, max_size: int = 10):
        self.items = []  # Lista para almacenar los elementos de la cola
        self.max_size = max_size  # Tamaño máximo de la cola

    def enqueue(self, item: int) -> bool:
        if self.is_full():
            return False  # La cola está llena, no se puede añadir más elementos
        self.items.append(item)
        return True  # Se añadió con éxito

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("La cola está vacía.")  # Error si la cola está vacía
        return self.items.pop(0)  # Eliminamos y devolvemos el primer elemento

    def head(self) -> int:
        if self.is_empty():
            raise IndexError("La cola está vacía.")
        return self.items[0]  # Devolvemos el primer elemento sin eliminarlo

    def is_empty(self) -> bool:
        return len(self.items) == 0  # Verdadero si la cola está vacía

    def is_full(self) -> bool:
        return len(self.items) >= self.max_size  # Verdadero si la cola está llena

    def expand(self, factor: int = 2) -> None:
        self.max_size *= factor  # Expandimos el tamaño máximo

    def dump_to_file(self, path: str) -> None:
        with open(path, "w") as f:
            f.write(",".join(map(str, self.items)))  # Escribimos los elementos en el archivo

    @classmethod
    def load_from_file(cls, path: str) -> "IntegerQueue":
        with open(path, "r") as f:
            elements = list(map(int, f.read().split(",")))
        queue = cls(max_size=len(elements))
        queue.items = elements
        return queue

    def __getitem__(self, index: int) -> int:
        return self.items[index]  # Devuelve el elemento en la posición indicada

    def __setitem__(self, index: int, item: int) -> None:
        self.items[index] = item  # Asigna el valor en la posición indicada

    def __add__(self, other: "IntegerQueue") -> "IntegerQueue":
        new_queue = IntegerQueue(max_size=self.max_size + other.max_size)
        new_queue.items = self.items + other.items  # Concatenamos los elementos de ambas colas
        return new_queue

    def __iter__(self):
        return IntegerQueueIterator(self)  # Devolvemos un iterador


class IntegerQueueIterator:
    def __init__(self, queue: IntegerQueue):
        self.queue = queue  # Referencia a la cola
        self.index = 0  # Índice para el recorrido

    def __next__(self) -> int:
        if self.index >= len(self.queue.items):
            raise StopIteration  # Si llegamos al final, detenemos la iteración
        item = self.queue.items[self.index]
        self.index += 1
        return item  # Devolvemos el siguiente elemento


# Prueba del código
if __name__ == "__main__":
    # Crear una cola e insertar elementos
    cola = IntegerQueue(max_size=5)
    cola.enqueue(1)
    cola.enqueue(2)
    cola.enqueue(3)

    # Mostrar el primer elemento
    print("Head:", cola.head())  # Head: 1

    # Eliminar un elemento
    print("Dequeue:", cola.dequeue())  # Dequeue: 1

    # Expandir la cola
    cola.expand(2)
    print("Nuevo tamaño máximo:", cola.max_size)  # Nuevo tamaño máximo: 10

    # Guardar en archivo y cargar desde archivo
    cola.dump_to_file("cola.txt")
    nueva_cola = IntegerQueue.load_from_file("cola.txt")
    print("Elementos de la nueva cola:", nueva_cola.items)  # Elementos: [2, 3]

    # Sumar dos colas
    cola2 = IntegerQueue(max_size=3)
    cola2.enqueue(4)
    cola2.enqueue(5)
    cola_suma = cola + cola2
    print("Cola suma:", cola_suma.items)  # Cola suma: [2, 3, 4, 5]

    # Iterar sobre la cola
    for item in cola:
        print("Iterando:", item)