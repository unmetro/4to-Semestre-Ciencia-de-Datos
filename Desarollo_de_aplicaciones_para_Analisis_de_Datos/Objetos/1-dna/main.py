class DNA:
    def __init__(self, sequence: str):
        """
        Constructor que inicializa la secuencia de ADN.
        """
        self.sequence = sequence

    def __len__(self) -> int:
        """
        Devuelve la longitud de la secuencia.
        """
        return len(self.sequence)

    def __str__(self) -> str:
        """
        Devuelve la secuencia como cadena de texto.
        """
        return self.sequence

    @property
    def adenines(self) -> int:
        """
        Cuenta el número de adeninas (A) en la secuencia.
        """
        return self.sequence.count('A')

    @property
    def cytosines(self) -> int:
        """
        Cuenta el número de citosinas (C) en la secuencia.
        """
        return self.sequence.count('C')

    @property
    def guanines(self) -> int:
        """
        Cuenta el número de guaninas (G) en la secuencia.
        """
        return self.sequence.count('G')

    @property
    def thymines(self) -> int:
        """
        Cuenta el número de timinas (T) en la secuencia.
        """
        return self.sequence.count('T')

    def __add__(self, other: 'DNA') -> 'DNA':
        # Determinamos la longitud de la secuencia más larga
        max_len = max(len(self.sequence), len(other.sequence))

        # Recorremos las secuencias posición por posición
        new_sequence = ''.join(
            max((self.sequence[i:i+1], other.sequence[i:i+1]))  # Sin default
            for i in range(max_len)
        )

        return DNA(new_sequence)


    def stats(self) -> dict[str, float]:
        """
        Calcula el porcentaje de cada base en la secuencia.
        """
        total = len(self.sequence)
        return {
            'A': self.adenines / total * 100,
            'C': self.cytosines / total * 100,
            'G': self.guanines / total * 100,
            'T': self.thymines / total * 100
        }

    def __mul__(self, other: 'DNA') -> 'DNA':
        """
        Multiplica dos secuencias, quedándose con las bases comunes
        (posición por posición).
        """
        new_sequence = ''.join(
            s if s == o else '' 
            for s, o in zip(self.sequence, other.sequence)
        )
        return DNA(new_sequence)

    @classmethod
    def build_from_file(cls, path: str) -> 'DNA':
        """
        Crea una instancia de DNA leyendo la secuencia desde un archivo.
        """
        with open(path, 'r') as file:
            sequence = file.readline().strip()
        return cls(sequence)

    def dump_to_file(self, path: str) -> None:
        """
        Guarda la secuencia en un archivo.
        """
        with open(path, 'w') as file:
            file.write(self.sequence)

    def __getitem__(self, index: int) -> str:
        """
        Devuelve la base que ocupa la posición indicada.
        """
        return self.sequence[index]

    def __setitem__(self, index: int, base: str) -> None:
        """
        Asigna una nueva base en la posición indicada.
        Si la base no es válida, se asigna 'A' por defecto.
        """
        if base not in "ACGT":
            base = 'A'  # Base por defecto: adenina
        self.sequence = (
            self.sequence[:index] + base + self.sequence[index + 1:]
        )

# Ejemplo de uso
dna1 = DNA("AGTC")
dna2 = DNA("TGCA")

# Imprimir las secuencias
print(dna1)  # AGTC
print(dna2)  # TGCA

# Sumar dos secuencias
suma = dna1 + dna2
print(suma)  # TGTC

# Multiplicar dos secuencias (bases comunes)
producto = dna1 * dna2
print(producto)  # G

# Mostrar estadísticas de una secuencia
print(dna1.stats())  # {'A': 25.0, 'C': 25.0, 'G': 25.0, 'T': 25.0}

# Modificar una base en una posición específica
dna1[0] = 'T'
print(dna1)  # TGTC

# Guardar la secuencia en un archivo
dna1.dump_to_file('dna_sequence.txt')

# Cargar una secuencia desde un archivo
dna3 = DNA.build_from_file('dna_sequence.txt')
print(dna3)  # TGTC
