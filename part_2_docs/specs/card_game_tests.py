import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.cardgame_1 = CardGame()
        self.card1 = Card("Heart", 5)
        self.card2 = Card("Spade", 3)
        self.card3 = Card("Diamond", 9)
   
   
    def test_card_has_value(self):
        self.assertEqual(3, self.card2.value)

    def test_card__has_suit(self):
       self.assertEqual("Heart", self.card1.suit)


    def test_cardgame_check_for_ace(self):
        self.assertEqual(False, self.cardgame_1.check_for_ace(self.card3))

    def test_cardgame_highest_card(self):
        self.assertEqual(self.card1, self.cardgame_1.highest_card(self.card1, self.card2))

    def test_cardgame_cards_total(self):
        cards = [self.card1, self.card2, self.card3]
        self.assertEqual("You have a total of 17", self.cardgame_1.cards_total(cards))
    

    