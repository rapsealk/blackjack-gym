#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import abc


class Player:

    __meta__ = abc.ABCMeta

    def __init__(self, initial_cash=10000):
        self.cash = initial_cash
        self.hand = []


class HumanPlayer(Player):

    def __init__(self):
        super(HumanPlayer, self).__init__()


class ComputerPlayer(Player):

    def __init__(self):
        super(ComputerPlayer, self).__init__()


if __name__ == "__main__":
    pass
