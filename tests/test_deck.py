from dealme.api import Deck, Card


def test_default_deck():
    # Standard deck size is 52 cards
    deck = Deck()
    assert len(deck) == 52


def test_card_created():
    card: Card = Card("♦", 2)
    deck: Deck = Deck()
    assert card in deck.deck


def test_fake_card_not_created():
    card: Card = Card("Fake", 2)
    deck: Deck = Deck()
    assert card not in deck.deck
