import tkinter as tk

from .cards import Card
from .string_wrappers import LanguageDependentString as lds
from .windows import MenuWindow, EntryWindow


class CardCreationWindow(MenuWindow):
    """Provides card creation options"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            lds("Choose the way to create a new card:",
                "Выбери способ создания карточки:"
            ), 
            {lds("Extract from file", "Из файла") : "DownloaderFromFileWindow",
             lds("Enter here", "Ввести тут") : "InputWindow"}
        )


class DownloaderFromFileWindow(EntryWindow):
    """Provides extract-from-file option as a part of card creation"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            lds("Enter the filepath here: ", "Введи путь до файла"),
            [lds("File path:", "Путь до файла:")],
            lds("Look for it!", "Найти!")
        )
    
    def do_action(self, file_path):
        super().do_action()
        self.controller.cards_manager.download_from_file(file_path)
        if self.controller.notification is not None:
            self.controller.raise_error(self.controller.notification)
        else:
            self.controller.call_success(lds(
                "Cards had been downloaded successfully!",
                "Карточки были успешно загружены!"
            ))


class InputWindow(EntryWindow):
    """Provides in-app card creation option"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            lds("Enter the word and the translation respectively here:",
                "Введи слово и перевот тут, соответственно"),
            [lds("Word:", "Слово:"), lds("Translation:", "Перевод:")],
            lds("Add the new card!", "Добавить новую карточку!")
        )
    
    def do_action(self, word, translation):
        super().do_action(self)
        self.controller.cards_manager.add_new_card(word, translation)
        self.controller.call_success(lds(
            "The card had been created successfully!",
            "Карточка была успешно создана!"
        ))
