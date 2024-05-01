import tkinter as tk

from .string_wrappers import LanguageDependentString as lds
from .windows import MenuWindow


class AchievementsWindow(MenuWindow):
    """Provides user achievement information sorted by frequency"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            lds("Here's your results. Good work!",
                "Ты хорошо поработал, вот твои результаты")
        )

        self.listbox = self.add_widget(
            tk.Listbox,
            self,
            {"height" : controller.YMAX, 
            "width" : controller.XMAX, 
            "font" : controller.font,
            "background" : controller.background_colour,
            "foreground" : controller.text_colour}
        )
        self.listbox.pack(expand=True)

    def tkraise(self, *args, **kwargs):
        sorted_cards = sorted(self.controller.cards_manager.get_data(), 
                              key=lambda item: -item.get_weight())
        self.listbox.config(listvariable=tk.Variable(
            value=[item.get_info() for item in sorted_cards])
        )
        super().tkraise(*args, **kwargs)
