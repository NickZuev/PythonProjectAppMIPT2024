import tkinter as tk

from Cards import Card
from WindowFactory import WindowsFactory


class CardCreationWindow(WindowsFactory):
    """Provides card creation options"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            "Choose the way to create a new card:", 
            {"Extract from file" : "ExtractorFromFileWindow",
             "Enter here" : "InputWindow"}
        )


class ExtractorFromFileWindow(WindowsFactory):
    """Provides extract-from-file option as a part of card creation"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            "Enter the filepath here: "
        )
        self.file_entry = tk.Entry(self, font=controller.font)
        self.button = tk.Button(
            self,
            font=controller.font,
            text="Look for it!",
            command=lambda: self.extract_from_file(self.file_entry.get()),
            background=controller.background_colour,
            foreground=controller.text_colour,
        )
        self.file_entry.pack()
        self.button.pack()
    
    def extract_from_file(self, file_path):
        """extracts list of cards in format \'word : translation\', used by button"""
        self.file_entry.delete(0, "end")
        with open(file_path, "r", encoding="utf8") as input_file:
            for line in input_file:
                try:
                    current_word, current_translation = line.strip().split(":")
                    self.controller.cards.append(Card(current_word,
                                                      current_translation))
                except:
                    pass
    
    def tkraise(self, *args, **kwargs):
        self.file_entry.config(background=self.controller.background_colour,
                               foreground=self.controller.text_colour)
        self.button.config(background=self.controller.background_colour,
                           foreground=self.controller.text_colour)
        super().config(background=self.controller.background_colour)
        super().tkraise(*args, **kwargs)


class InputWindow(WindowsFactory):
    """Provides in-app card creation option"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            "Enter the word and the translation respectively here:"
        )
        self.word_entry = tk.Entry(self, font=controller.font)
        self.translation_entry = tk.Entry(self, font=controller.font)
        self.button = tk.Button(
            self,
            font=controller.font,
            text="Add the new card!",
            command=lambda: self.add_new_card(self.word_entry.get(), 
                                              self.translation_entry.get())
        )
        self.word_entry.pack()
        self.translation_entry.pack()
        self.button.pack()
    
    def add_new_card(self, word, translation):
        """adds new card in app, used by button"""
        self.controller.cards.append(Card(word, translation))
        self.word_entry.delete(0, "end")
        self.translation_entry.delete(0, "end")
    
    def tkraise(self, *args, **kwargs):
        self.word_entry.config(background=self.controller.background_colour,
                               foreground=self.controller.text_colour)
        self.translation_entry.config(background=self.controller.background_colour,
                                      foreground=self.controller.text_colour)
        self.button.config(background=self.controller.background_colour,
                           foreground=self.controller.text_colour)
        super().config(background=self.controller.background_colour)
        super().tkraise(*args, **kwargs)
