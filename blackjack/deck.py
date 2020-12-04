#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from card import Card


class Deck:

    def __init__(self, joker=False):
        self.cards = []
        for suit in Card.Suit:
            for rank in Card.Rank:
                self.cards.append(Card(suit, rank))


if __name__ == "__main__":
    deck = Deck()
    print(deck.cards[0])
    print(len(deck.cards))
