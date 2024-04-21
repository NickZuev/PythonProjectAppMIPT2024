import tkinter as tk
from tkinter import font as tkfont

from Cards import *
from WindowFactory import WindowsFactory
from HelpWindow import HelpWindow
from SettingsWindow import *
from CardCreationWindow import *
from AchievementsWindow import AchievementsWindow


class App(tk.Tk):
    """Main part of the project, manages the whole process"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.YMAX = self.winfo_screenheight()
        self.XMAX = self.winfo_screenwidth()

        self.title("English Cards")

        self.geometry(f'{self.XMAX}x{self.YMAX}')

        self.font = tkfont.Font(family='Helvetica', size=18)

        self.background_colour = "white"

        self.text_colour = "black"

        self.BASE = 3

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.cards = []
        self.current_card = None
        self.state = None

        self.frames = {}
        for F in (HelpWindow, AchievementsWindow, MenuWindow,
                  SettingsWindow, SetupColorWindow, CardsWindow,
                  CardCreationWindow, ExtractorFromFileWindow,
                  InputWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.current_frame = None

        self.change_window("MenuWindow")
        

    def change_window(self, window_name):
        """switch windows(frames)"""
        self.current_frame = self.frames[window_name]
        self.current_frame.tkraise()
    
    def apply(self, function, *args):
        """use fuction(*args) in current window if possible, used by key-binds"""
        try:
            getattr(self.current_frame, function)(*args)
        except:
            #print(f'apply log: {function}({args}) was used in inappropriate context')
            pass


class MenuWindow(WindowsFactory):
    """Start page, provides all user-necessary access"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            "Menu", 
            {"Cards" : "CardsWindow", 
             "Create new card" : "CardCreationWindow",
             "Achievements" : "AchievementsWindow", 
             "Settings" : "SettingsWindow", 
             "Help" : "HelpWindow"}
        )
