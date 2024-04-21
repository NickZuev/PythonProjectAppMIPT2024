import tkinter as tk

from Cards import Card
from WindowFactory import WindowsFactory


class AchievementsWindow(WindowsFactory):
    """Provides user achievement information sorted by frequency"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            "Here's your results. Good work!"
        )
        self.listbox = tk.Listbox(
            self, 
            height=controller.YMAX, 
            width=controller.XMAX, 
            font=controller.font
        )
        self.listbox.pack(expand=True)

    def tkraise(self, *args, **kwargs):
        tmp = [f'weight : {item.get_weight()} | card : {item.get(1)} -- {item.get(0)}'
               for item in sorted(self.controller.cards, 
                                  key=lambda item: -item.get_weight())]
        self.listbox.config(
            listvariable=tk.Variable(value=tmp), 
            background=self.controller.background_colour,
            foreground=self.controller.text_colour
        )
        super().tkraise(*args, **kwargs)
