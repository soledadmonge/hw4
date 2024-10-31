import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hw5_lib', 'hw5_lib')))

sys.path.append(os.path.abspath("../")) 
from hw5 import Card, Deck

# %%
def test__card():
    card = Card('Hearts', 'A')
    
    assert card.suit == 'Hearts', "Suit must be 'Hearts'"
    assert card.value == 'A', "The value must be 'A'"

# %%
def test__deck():
    deck = Deck()
    t_suits = {'Hearts', 'Diamonds', 'Clubs', 'Spades'}
    t_values = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}

    assert {card.suit for card in deck.cards} == t_suits, "The Deck must have all the suits"
    assert {card.value for card in deck.cards} == t_values, "The Deck must have all de values"
    assert len(deck.cards) == 52, "The Deck must have 52 cards"



