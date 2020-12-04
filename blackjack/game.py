#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import gym


class Game(gym.Env):

    class Result:
        BLACKJACK = 0
        HIT = 1
        STAND = 2
        BUST = 3

    def __init__(self):
        super(Game, self).__init__()


if __name__ == "__main__":
    pass
