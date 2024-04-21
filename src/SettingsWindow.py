import tkinter as tk

from WindowFactory import WindowsFactory


class SettingsWindow(WindowsFactory):
    """Provides some customizations"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            "Settings", 
            {"Set up color" : "SetupColorWindow"}
        )


class SetupColorWindow(WindowsFactory):
    """Provides setting up color scheme as a part of settings"""
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Set up color:")
        self.buttons = [
            tk.Button(
                self, 
                text="White-Black", 
                font=controller.font,
                command=lambda: self.change_color("white", "black"),
                background=controller.background_colour,
                foreground=controller.text_colour,
                width=controller.YMAX
            ),
            tk.Button(
                self, 
                text="Black-Green", 
                font=controller.font,
                command=lambda: self.change_color("black", "green"),
                background=controller.background_colour,
                foreground=controller.text_colour,
                width=controller.YMAX
            )
        ]
        for button in self.buttons:
            button.pack()
    
    def change_color(self, background_colour, text_colour):
        """changes color scheme of the whole app, used by buttons"""
        self.controller.background_colour = background_colour
        self.controller.text_colour = text_colour
        self.config(background=background_colour)
        self.controller.config(background=background_colour)
        self.controller.change_window("SetupColorWindow")
    
    def tkraise(self, *args, **kwargs):
        for button in self.buttons:
            button.config(background=self.controller.background_colour,
                          foreground=self.controller.text_colour)
        super().tkraise(*args, **kwargs)

