import functools

import tkinter as tk


class WindowsFactory(tk.Frame):
    """Factory programming template used to create windows(frames)"""
    def __init__(self, parent, controller, text, buttons_settings = dict()):
        tk.Frame.__init__(
            self, 
            parent, 
            background=controller.background_colour
        )
        self.controller = controller
        self.label = tk.Label(
            self, 
            text=text, 
            font=controller.font,
            background=controller.background_colour,
            foreground=controller.text_colour,
            width=controller.YMAX
        )
        self.label.pack()
        self.buttons = []
        for button_text, class_name in buttons_settings.items():
            button = tk.Button(
                self, 
                text=button_text, 
                font=controller.font,
                command=functools.partial(controller.change_window, 
                                          class_name),
                background=controller.background_colour,
                foreground=controller.text_colour,
                width=controller.YMAX
            )
            button.pack()
            self.buttons.append(button)
    
    def tkraise(self, *args, **kwargs):
        self.label.config(background=self.controller.background_colour,
                          foreground=self.controller.text_colour)
        for button in self.buttons:
            button.config(background=self.controller.background_colour,
                          foreground=self.controller.text_colour)
        super().config(background=self.controller.background_colour)
        super().tkraise(*args, **kwargs)

