#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import numpy as np

from deck import Deck


class Dealer:

    def __init__(self, deck=None):
        if deck is None:
            deck = Deck()
        np.random.shuffle(deck.cards)
        self.deck = deck


if __name__ == "__main__":
    pass
