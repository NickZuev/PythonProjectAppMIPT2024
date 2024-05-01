import tkinter as tk
from random import choices

from .string_wrappers import LanguageDependentString as lds


class Card:
    """Store and operate card information"""
    def __init__(self, word, translation, weight = 1):
        self.word = word
        self.translation = translation
        self.weight = weight
    
    def get_info(self):
        """Give information about card in certain format"""
        return f'{self.weight} | {self.word} : {self.translation}'
    
    def increment(self):
        """decreases card frequency"""
        self.weight += 1
    
    def decrement(self):
        """increases card frequency"""
        self.weight -= 1

    def get(self, state):
        """provides ability to get information from instance"""
        return self.word if state else self.translation

    def get_weight(self):
        """provides ability to get frequency from instance"""
        return self.weight


class CardsManager:
    """Manages all card-linked processes"""
    def __init__(self, controller):
        self.controller = controller
        self.data = []
        self.BASE = 3
    
    def get_data(self, index = None):
        """provides ability to get data from instance"""
        if index is None:
            return self.data
        return self.data[index]
    
    def get_new_card(self, count = 1):
        """returns \"count\" new cards based on cards frequency"""
        if self.is_valid_call():
            return choices(
                self.data, 
                weights=[self.BASE ** -item.get_weight()
                         for item in self.data],
                k=count
            )
        return None
    
    def is_valid_call(self):
        """checks whether there are any cards"""
        if self.data == []:
            self.controller.raise_error(lds(
                ("No cards were created. "
                "Check \"Create new card\" window first"),
                ("Никаких карточек не было создано. "
                "Зайди в окно \"Создать новую карточку\" сначала")
            ))
            return False
        return True
    
    def download_from_file(self, file_path):
        """downloads data from \"file_path\" file"""
        try:
            with open(file_path, "r", encoding="utf8") as input_file:
                new_cards = []
                for line in input_file:
                    try:
                        weight = 1
                        word, translation = line.split(":")
                        if '|' in word:
                            weight, word = word.split('|')
                        new_cards.append(Card(
                            word.strip(), 
                            translation.strip(), 
                            int(weight)
                        ))
                    except:
                        self.controller.notification = lds(
                            """
                            There is a format mismatch somewhere in your file. 
                            Please, use the format \"word : translation\"""",
                            """
                            Где-то в файле есть несоответствие формату
                            Пожалуйста, используй формат \"слово : перевод\""""
                        )
                        return
                self.data.extend(new_cards)
        except:
            self.controller.notification = lds(
                "Wrong path file, try to enter it once again",
                "Неправильный путь до файла, попробуй ввести ещё раз"
            )
    
    def add_new_card(self, word, translation):
        """creates and add a new card"""
        self.data.append(Card(word, translation))
    
    def upload_to_file(self, file_path):
        """uploads data to \"file_path\" file"""
        with open(file_path, "w", encoding="utf8") as output_file:
            for card in self.data:
                output_file.write(card.get_info() + '\n')
    
    def find(self, word):
        """finds whether wuch word exist as word or translation"""
        for item in self.data:
            if item.get(0) == word or item.get(1) == word:
                return item
        return None
