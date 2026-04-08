from dataclasses import dataclass
from itertools import product


@dataclass
class Card:
    suit: str
    value: int


class Deck:
    """Represents a deck of cards."""

    def __init__(self, suits: list[str] | None = None, values: list[int] | None = None):
        """Creates a deck of cards with suits and values.

        Args:
            suits: Suits of cards for deck to have.
            values: Values of cards for deck to have.
        """

        self.suits = suits
        self.values = values
        if self.suits is None:
            self.suits = ["♠", "♥", "♣", "♦"]
        if self.values is None:
            self.values = list(range(1, 14))
        self.deck: list[Card] = []
        for suit, value in product(self.suits, self.values):
            card = Card(suit, value)
            self.insert(card)

    def insert(self, card: Card, index: int = 0):
        """Inserts a card into the deck.

        Args:
          card: Card to insert.
          index: Where to insert the card, inserts at the top by default.
        """
        self.deck.insert(index, card)

    def deal(self, index: int = 0) -> Card:
        """Deals a card from the deck.

        Args:
          index: Where to deal the card from, deals from the top by default.
        Returns:
            Card: The card that was removed from the deck.
        """
        card: Card = self.deck.pop(index)
        return card

    def __len__(self) -> int:
        """Returns the size of the deck."""
        return len(self.deck)
