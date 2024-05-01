import tkinter as tk

from .windows import MenuWindow, EntryWindow
from .string_wrappers import LanguageDependentString as lds


class SettingsWindow(MenuWindow):
    """Provides some customizations"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            lds("Settings", "Настройки"),
            {lds("Set up color", "Установите цвет") : "SetupColorWindow",
             lds("Change language", "Изменить язык") : "LanguageChangingWindow"}
        )


class SetupColorWindow(EntryWindow):
    """Provides setting up color scheme as a part of settings"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            lds(("Entry colors you'd like background and text to be\n"
                 "You may use RGB format"),
                ("Введите цвета фона и текста\n"
                 "Можно использовать RGB формат")),
            [lds("Background:", "Фоновый:"), 
             lds("Text:", "Текстовый:")],
            lds("Change colour!", "Изменить цвет!")
        )
    
    def do_action(self, background_colour, text_colour):
        super().do_action()
        previous_background_colour = str(self.controller.background_colour)
        previous_text_colour = str(self.controller.text_colour)
        try:
            self.controller.config(background=background_colour)
            self.config(background=background_colour)
            self.controller.background_colour.set(background_colour)
            self.controller.text_colour.set(text_colour)
            self.tkraise()
        except:
            self.controller.config(background=previous_background_colour)
            self.config(background=previous_background_colour)
            self.controller.background_colour.set(previous_background_colour)
            self.controller.text_colour.set(previous_text_colour)
            self.tkraise()
            self.controller.raise_error(lds(
                "I've mistaken - it's not a color!",
                "Ты ошибся - это не цвет!"
            ))


class LanguageChangingWindow(MenuWindow):
    """Provides language changing as a part of settings"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            lds("Choose the language:", "Выберите язык:")
        )
        self.buttons_texts = [
            lds("English", "Английский"),
            lds("Russian", "Русский")
        ]
        self.buttons = [
            self.add_widget(
                tk.Button,
                self, 
                {'text' : self.buttons_texts[0], 
                'font' : controller.font,
                'command' : lambda: (lds.set("english"), self.tkraise()),
                'activebackground' : self.controller.background_colour,
                'activeforeground' : self.controller.text_colour,
                'background' : controller.background_colour,
                'foreground' : controller.text_colour,
                'width' : controller.YMAX}
            ),
            self.add_widget(
                tk.Button,
                self, 
                {'text' : self.buttons_texts[1], 
                'font' : controller.font,
                'command' : lambda: (lds.set("russian"), self.tkraise()),
                'activebackground' : self.controller.background_colour,
                'activeforeground' : self.controller.text_colour,
                'background' : controller.background_colour,
                'foreground' : controller.text_colour,
                'width' : controller.YMAX}
            ),
        ]
        for button in self.buttons:
            button.pack()
