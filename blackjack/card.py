#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import enum


class Card:

    class Suit(enum.Enum):
        CLUB    = '♣'  # noqa: E221
        DIAMOND = '♦'
        HEART   = '♥'  # noqa: E221
        SPADE   = '♠'  # noqa: E221

    class Rank(enum.Enum):
        KING = 'K'
        QUEEN = 'Q'
        JACK = 'J'
        ACE = 'A'
        RANK02 = '2'
        RANK03 = '3'
        RANK04 = '4'
        RANK05 = '5'
        RANK06 = '6'
        RANK07 = '7'
        RANK08 = '8'
        RANK09 = '9'
        RANK10 = '10'
        JOKER = 'Joker'

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{suit} {rank}'.format(suit=self.suit.value, rank=self.rank)


if __name__ == "__main__":
    card = Card(Card.Suit.CLUB, Card.Rank.ACE)
    print('Card:', card)
