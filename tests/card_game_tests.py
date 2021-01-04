import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.ace_of_spades = Card("spades", 1)
        self.two_of_hearts = Card("hearts", 2)


    def test_check_for_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.ace_of_spades))

    def test_check_is_not_ace(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.two_of_hearts))

    def test_highest_card(self):
        self.assertEqual(self.two_of_hearts, CardGame.highest_card(self, self.ace_of_spades, self.two_of_hearts))

    def test_cards_total(self):
        cards = [self.ace_of_spades, self.two_of_hearts]
        self.assertEqual("You have a total of 3", CardGame.cards_total(self, cards))