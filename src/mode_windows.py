import functools
from random import shuffle, randint

import tkinter as tk

from .windows import MenuWindow, TextWindow, EntryWindow
from .string_wrappers import LanguageDependentString as lds


CARDS_ADVISE = lds(
    ("Press left arrow to get a new english word\n"
     "Press right arrow to get a new russian word\n"
     "Press up arrow to decrease the card frequency\n"
     "Press down arrow to increase the card frequency\n"
     "Press space to flip the card\n"
     "But at first create some cards with \"Create new card\" option"),
    ("Нажми левую стрелку, чтобы получить новое английское слово\n"
     "Нажми правую стрелку, чтобы получить новое русское слово\n"
     "Нажми стрелку вверх, чтобы понизить частоту встречаемости\n"
     "Нажми стрелку вниз, чтобы повысить частоту встречаемости\n"
     "Нажми пробел, чтобы перевернуть карточку\n"
     "Но сначала создай карточку с помощью \"Создать новую карточку\"")
)

class ModeSelectionWindow(MenuWindow):
    """Provides mode choice option"""
    def __init__(self, parent, controller):
        super().__init__(
            parent,
            controller,
            lds("Choose your way to memorize", "Как тебе удобнее запоминать?"),
            {lds("Classic cards", "Классические карточки") : "CardsModeWindow",
             lds("Match mode", "Совмести") : "MatchModeSettingsWindow",
             lds("Write mode", "Диктант") : "WriteModeWindow"}
        )


class CardsModeWindow(TextWindow):
    """Responsible for \"cards\"-mode"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller,
            CARDS_ADVISE
        )
        self.configuration = None
        self.manager = self.controller.cards_manager

    def is_valid_change(self):
        """checks whether current_card is defined"""
        if not self.manager.is_valid_call() and self.configuration is None:
            self.controller.raise_error(lds(
                "Which card you're trying to change(flip)?",
                "Какую карточку ты хочешь изменить(перевернуть)?"
            ))
            return False
        return True

    def get_next_card(self, state):
        """randomly gets new card, used by App.apply()"""
        if self.manager.is_valid_call():
            self.configuration = [self.manager.get_new_card()[0], state]
            self.tkraise()
    
    def flip(self):
        """flips current card, used by App.apply()"""
        if self.is_valid_change():
            self.configuration[1] = 1 - self.configuration[1]
            self.tkraise()
    
    def increment(self):
        """decreases current card frequency, used by App.apply()"""
        if self.is_valid_change():
            self.configuration[0].increment()

    def decrement(self):
        """increases current card frequency, used by App.apply()"""
        if self.is_valid_change():
            self.configuration[0].decrement()
    
    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        if self.configuration is not None:
            self.label.config(
                text=self.configuration[0].get(self.configuration[1])
            )


class MatchModeSettingsWindow(EntryWindow):
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller,
            lds(("Entry match mode dimentions \n"
                 "Mind that words might turn out to be out of borders "
                 "and total number of button should be even"),
                ("Введите размеры поля \n"
                 "Следите, чтобы все слова поместились в размеры кнопок "
                 "и общее количество клеток должны быть чётным")),
            [lds("Column count:", "Количество стобцов:"),
             lds("Row count:", "Количество строк:")],
            lds("Get started!", "Начать!")
        )
    
    def do_action(self, columns_count, rows_count):
        try:
            columns_count = int(columns_count)
            rows_count = int(rows_count)
        except:
            self.controller.raise_error(lds(
                "Please, enter integers!",
                "Пожалуйста, введите числа!"
            ))
            return
        if columns_count * rows_count % 2 == 1:
            self.controller.raise_error(lds(
                "Total number of cells is odd, but must be even!",
                "Общее количество клеток нечётно, а должно быть чётно!"
            ))
        elif self.controller.cards_manager.is_valid_call():
            self.controller.frames['MatchModeWindow'].rows_count = rows_count
            self.controller.frames['MatchModeWindow'].columns_count = columns_count
            self.controller.change_window('MatchModeWindow')


class MatchModeWindow(MenuWindow):
    """Responsible for \"match\"-mode"""
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.manager = self.controller.cards_manager
        self.rows_count = 0
        self.columns_count = 0
        self.count = 0
        self.buttons = []
        self.pressed_button = None
        
    
    def make_pressed(self, i, j):
        """action for pressed button"""
        button = self.buttons[i * self.columns_count + j]
        button.config(state='disabled')
        if self.pressed_button is None:
            self.pressed_button = button
            return
        card1 = self.manager.find(button['text'])
        card2 = self.manager.find(self.pressed_button['text'])
        if card1 is card2:
            self.count -= 2
            card1.decrement()
            button.config(text="")
            self.pressed_button.config(text="")
        else:
            card1.increment()
            card2.increment()
            button.config(state='normal')
            self.pressed_button.config(state='normal')
        self.pressed_button = None
        if self.count == 0:
            self.controller.call_success(lds(
                "You've matched all words. Otto boy/girl!",
                "Ты смог совместить все слова. Молодец!"
            ))
        
    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        self.count = self.rows_count * self.columns_count
        cards = self.manager.get_new_card(self.count // 2)
        texts = [item.get(0) for item in cards] + \
                [item.get(1) for item in cards]
        shuffle(texts)
        for button in self.buttons:
            del button
        for i in range(self.rows_count):
            for j in range(self.columns_count):
                self.buttons.append(self.add_widget(
                    tk.Button,
                    self,
                    {'font' : self.controller.font,
                    'text' : texts[i * self.columns_count + j],
                    'command' : functools.partial(self.make_pressed, i, j),
                    'activebackground' : self.controller.background_colour,
                    'activeforeground' : self.controller.text_colour,
                    'background' : self.controller.background_colour,
                    'foreground' : self.controller.text_colour}
                ))
                self.buttons[i * self.columns_count + j].place(
                    relx=1/self.rows_count * i,
                    rely=1/self.columns_count * j,
                    relwidth=1/self.rows_count,
                    relheight=1/self.columns_count
                )


class WriteModeWindow(EntryWindow):
    """Responsible for \"cards\"-mode"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller,
            lds("", ""),
            [lds("Entry translation:", "Введите перевод:")],
            lds("Check!", "Проверить!")
        )
        self.configuration = None
        self.manager = self.controller.cards_manager

    def do_action(self, word):
        super().do_action()
        if self.configuration[0].get(1 - self.configuration[1]) == word:
            self.configuration[0].increment()
            self.tkraise()
        else:
            self.configuration[0].decrement()
    
    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        if self.manager.is_valid_call():
            self.configuration = [
                self.manager.get_new_card()[0], 
                randint(0, 1)
            ]
            self.widgets[0][0].config(
                text=self.configuration[0].get(self.configuration[1])
            )