import tkinter as tk
from random import choices

from WindowFactory import WindowsFactory


CARDS_ADVISE = """press:
    Left arrow to get a new english word
    Right arrow to get a new russian word
    Up arrow to increase the card frequency
    Down arrow to decrease the card frequency 
    but at first create some cards with \"Create new card\" option"""


class Card:
    """Store and operate card information"""
    def __init__(self, word, translation):
        self.weight = 1
        self.word = word
        self.translation = translation
    
    def increment(self):
        """increases card frequency"""
        self.weight += 1
    
    def decrement(self):
        """decreases card frequency"""
        self.weight -= 1

    def get(self, state):
        """provides ability to get information from instance"""
        return self.word if state else self.translation

    def get_weight(self):
        """provides ability to get frequency from instance"""
        return self.weight


class CardsWindow(WindowsFactory):
    """Responsible for all cards-linked processes"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            CARDS_ADVISE
        )

    def get_next_card(self, state):
        """randomly gets new card, used by App.apply()"""
        self.controller.current_card = choices(
            self.controller.cards, 
            weights=[self.controller.BASE ** -item.get_weight() 
                     for item in self.controller.cards]
        )[0]
        self.controller.state = state
        self.label.config(
            text=self.controller.current_card.get(self.controller.state)
        )
    
    def flip(self):
        """flips current card, used by App.apply()"""
        self.controller.state = 1 - self.controller.state
        self.label.config(
            text=self.controller.current_card.get(self.controller.state)
        )
    
    def increment(self):
        """increases current card frequency, used by App.apply()"""
        self.controller.current_card.increment()

    def decrement(self):
        """decreases current card frequency, used by App.apply()"""
        self.controller.current_card.decrement()


