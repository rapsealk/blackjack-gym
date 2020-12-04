#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import unittest

from blackjack_gym import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_a(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
