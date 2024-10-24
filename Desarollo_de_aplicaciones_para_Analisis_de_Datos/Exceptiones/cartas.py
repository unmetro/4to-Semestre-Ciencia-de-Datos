class InvalidCardError(Exception):
    """Excepción personalizada para cartas inválidas."""

    def __init__(self, message: str = ''):
        super().__init__(f'Invalid card: {message if message else "Invalid card"}')

    def __str__(self):
        return self.args[0]

class Card:
    """Clase que representa una carta de poker."""
    
    # Definimos los valores posibles para las cartas
    VALUE_MAP = {
        'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, 
        '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
        'J': 11, 'Q': 12, 'K': 13
    }
    
    SUITS = ['♠', '♦', '♥', '♣']

    def __init__(self, value: int | str, suit: str):
        # Validamos el valor
        if isinstance(value, str) and value in self.VALUE_MAP:
            self.value = self.VALUE_MAP[value]
        elif isinstance(value, int) and 1 <= value <= 13:
            self.value = value
        else:
            raise InvalidCardError(f'{repr(value)} is not a supported value')
        
        # Validamos el palo
        if suit not in self.SUITS:
            raise InvalidCardError(f'{repr(suit)} is not a supported suit')
        
        self.suit = suit

    def __repr__(self):
        """Devuelve el glifo de la carta."""
        return f'{self.value} {self.suit}'

    def __eq__(self, other: object) -> bool:
        """Indica si dos cartas son iguales."""
        if not isinstance(other, Card):
            return False
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other: 'Card') -> bool:
        """Indica si una carta es menor que otra."""
        return self.value < other.value

    def __gt__(self, other: 'Card') -> bool:
        """Indica si una carta es mayor que otra."""
        return self.value > other.value

    def __add__(self, other: 'Card') -> 'Card':
        """Devuelve una nueva carta como suma de dos cartas."""
        new_value = self.value + other.value
        new_value = 1 if new_value > 13 else new_value  # Se convierte en As si supera 13

        new_suit = self.suit if self > other else other.suit
        return Card(new_value, new_suit)

    @classmethod
    def get_available_suits(cls) -> str:
        """Devuelve los palos disponibles."""
        return ', '.join(cls.SUITS)

    @classmethod
    def get_cards_by_suit(cls, suit: str):
        """Genera todas las cartas de un palo específico."""
        if suit not in cls.SUITS:
            raise InvalidCardError(f'{repr(suit)} is not a supported suit')
        for value in cls.VALUE_MAP.keys():
            yield Card(value, suit)

# Ejemplo de uso
try:
    carta1 = Card('A', '♠')
    carta2 = Card(13, '♦')
    print(carta1)  # A ♠
    print(carta2)  # 13 ♦
    print(carta1 + carta2)  # 1 ♠ (porque A + K es 14, y se convierte en As)
except InvalidCardError as e:
    print(e)
