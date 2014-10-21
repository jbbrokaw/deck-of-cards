"""Tests deck and card objects from deck.py
can be run with py.test
"""
from __future__ import unicode_literals

import pytest  # For exception testing

import deck
from deck import Card
from deck import Deck


def test_card_init():
    """Card(suit, value), where suit is 0-3, value is 0-12
    Card(0, 0) should be the ace of hearts, etc."""
    with pytest.raises(TypeError):
        Card()
    with pytest.raises(TypeError):
        Card(1)
    with pytest.raises(ValueError):
        Card(5, 0)  # Suit is out of range
    with pytest.raises(ValueError):
        Card(1, 13)  # Value is out of range

    card = Card(0, 0)
    assert card.suit == 0
    assert card.value == 0
    assert deck.SUIT_NAMES[card.suit] == "Hearts"
    assert deck.VALUE_NAMES[card.value] == "Ace"


def test_card_comparability():
    """Want to be able to tell if cards are identical, which one is better"""
    assert Card(0, 0) == Card(0, 0)
    assert Card(0, 4) > Card(3, 3)  # A three beats a two
    # Same vals tie regardless of suit but are not equal
    assert not Card(0, 4) > Card(1, 4)
    assert not Card(0, 4) < Card(1, 4)
    assert not Card(0, 4) == Card(1, 4)
    assert Card(0, 0) > Card(0, 12)  # An ace beats a king


def test_deck_init():
    """Deck() should initialize a standard 52-card deck"""
    with pytest.raises(TypeError):
        Deck(100)  # No values allowed (for now)

    Deck()  # Should not raise error


def test_deck_iterability():
    """Let's make it iterable"""
    deck = Deck()
    for i, card in enumerate(deck):
        print i, card
        assert card == Card(i // 13, i % 13)


def test_deck_length():
    deck = Deck()
    assert len(deck) == 52  # Want to be able to see its size


def test_deck_deal():
    """Want to be able to get the top card (and 'remove' it)"""
    deck = Deck()
    with pytest.raises(TypeError):
        deck.deal(1)  # No values (for now)
    # Not shuffled, all cards should be in order
    topcard = deck.deal()  # Should be ace of hearts, Card(0, 0)
    assert topcard == Card(0, 0)
    nextcard = deck.deal()  # Should be two of hearts, Card(0, 1)
    assert nextcard == Card(0, 1)


def test_deck_shuffle():
    """Want to be able to shuffle it"""
    deck = Deck()
    with pytest.raises(TypeError):
        deck.shuffle(1)  # No values (for now)
    unmoved_cards = 0
    deck.shuffle()
    for i in xrange(52):
        card = deck.deal()
        if card == Card(i // 13, i % 13):
            unmoved_cards += 1
    print unmoved_cards
    assert unmoved_cards < 5  # It would be weird if this was higher
