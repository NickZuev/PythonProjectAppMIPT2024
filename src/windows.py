import functools

import tkinter as tk


class Window(tk.Frame):
    """Used to create windows(frames)"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(
            self, 
            parent, 
            background=controller.background_colour
        )
        self.controller = controller
        self.widgets = []
    
    def add_widget(self, Widget, parent, kwargs):
        """adds new widget with its configuration to the window"""
        self.widgets.append((Widget(parent, **kwargs), kwargs))
        return self.widgets[-1][0]
    
    def tkraise(self, *args, **kwargs):
        super().config(background=self.controller.background_colour)
        for widget, configuration in self.widgets:
            widget.config(**configuration)
        super().tkraise(*args, **kwargs)


class MenuWindow(Window):
    """Used to create menu windows(frames)"""
    def __init__(self, parent, controller, text = None, buttons_settings = dict()):
        super().__init__(parent, controller)
        if text is not None:
            self.label = self.add_widget(
                tk.Label,
                self,
                {'text' : text, 
                'font' : self.controller.font,
                'background' : self.controller.background_colour,
                'foreground' : self.controller.text_colour,
                'width' : self.controller.YMAX}
            )
            self.label.pack()
        self.buttons = []
        for button_text, class_name in buttons_settings.items():
            self.buttons.append(self.add_widget(
                tk.Button,
                self,
                {'text' : button_text, 
                'font' : controller.font,
                'command' : functools.partial(controller.change_window, class_name),
                'activebackground' : self.controller.background_colour,
                'activeforeground' : self.controller.text_colour,
                'background' : controller.background_colour,
                'foreground' : controller.text_colour,
                'width' : controller.YMAX}
            ))
            self.buttons[-1].pack()


class EntryWindow(Window):
    """Used to create windows(frames) with entries windgets"""
    def __init__(self, parent, controller, text, entry_settings, button_text):
        super().__init__(parent, controller)
        self.add_widget(
            tk.Label,
            self,
            {'text' : text, 
            'font' : self.controller.font,
            'background' : self.controller.background_colour,
            'foreground' : self.controller.text_colour}
        ).pack()
        i = 1
        self.entries = []
        for current_text in entry_settings:
            frame = tk.Frame(self, parent, background="cyan")
            self.add_widget(
                tk.Label,
                frame,
                {'text' : current_text, 
                'font' : self.controller.font,
                'background' : self.controller.background_colour,
                'foreground' : self.controller.text_colour}
            ).pack(side='left')
            self.entries.append(self.add_widget(
                tk.Entry, 
                frame, 
                {'font' : self.controller.font,
                'background' : self.controller.background_colour,
                'foreground' : self.controller.text_colour}
            ))
            self.entries[-1].pack(side='right')
            frame.pack()
            i += 1
        self.button = self.add_widget(
            tk.Button,
            self,
            {'text' : button_text, 
            'font' : controller.font,
            'command' : lambda: self.do_action(
                *[entry.get() for entry in self.entries]
            ),
            'activebackground' : self.controller.background_colour,
            'activeforeground' : self.controller.text_colour,
            'background' : controller.background_colour,
            'foreground' : controller.text_colour}
        )
        self.button.pack()
    
    def do_action(self, *args):
        """performs the respective action"""
        for entry in self.entries:
            entry.delete(0, "end")


class TextWindow(Window):
    """Used to create windows(frames) with only one label field"""
    def __init__(self, parent, controller, text):
        super().__init__(parent, controller)
        self.label = self.add_widget(
            tk.Label,
            self,
            {'text' : text, 
            'font' : self.controller.font,
            'background' : self.controller.background_colour,
            'foreground' : self.controller.text_colour}
        )
        self.label.place(relx=0.5, rely=0.5, anchor='center')
