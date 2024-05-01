import tkinter as tk
from tkinter import font as tkfont

from .cards import CardsManager
from .windows import MenuWindow
from .help_window import HelpWindow
from .settings_windows import *
from .card_creation_windows import *
from .achievements_window import AchievementsWindow
from .notification_window import NotificationWindow
from .mode_windows import *
from .string_wrappers import LanguageDependentString as lds, StringReference as rstring


class App(tk.Tk):
    """Main part of the project, manages the whole process"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.YMAX = self.winfo_screenheight()
        self.XMAX = self.winfo_screenwidth()
        self.attributes('-fullscreen', True)
        self.title("English Cards")
        self.geometry(f'{self.XMAX}x{self.YMAX}')

        self.font = tkfont.Font(family='Helvetica', size=18)
        self.background_colour = rstring("white")
        self.text_colour = rstring("black")
        #self.image = tk.PhotoImage(file='transparent_image.png')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.cards_manager = CardsManager(self)

        self.frames = {}
        for F in (HelpWindow, AchievementsWindow, MainWindow,
                  SettingsWindow, SetupColorWindow, CardsModeWindow, 
                  CardCreationWindow, DownloaderFromFileWindow,
                  InputWindow, NotificationWindow, WriteModeWindow, 
                  LanguageChangingWindow, MatchModeWindow, 
                  ModeSelectionWindow, MatchModeSettingsWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.current_frame = None

        self.error_code = None
        self.windows_stack = []

        self.change_window("MainWindow")
        self.data_storage = "assets/data.txt"
        self.cards_manager.download_from_file(self.data_storage)
        

    def change_window(self, window_name):
        """switch windows(frames)"""
        self.current_frame = self.frames[window_name]
        self.current_frame.tkraise()
        if len(self.windows_stack) == 0 or \
                self.windows_stack[-1] != "NotificationWindow":
            self.windows_stack.append(window_name)
    
    def apply(self, function, *args):
        """use fuction(*args) in current window if possible, used by key-binds"""
        if function in dir(self.current_frame):
            getattr(self.current_frame, function)(*args)

    def exit(self, code):
        """close window with saving data"""
        self.cards_manager.upload_to_file(self.data_storage)
        exit(code)

    def undo(self):
        """returns to the previous window if exists else call exit"""
        self.windows_stack.pop()
        if self.windows_stack == []:
            self.exit(0)
        else:
            self.change_window(self.windows_stack.pop())
    
    def raise_error(self, error_code):
        """display error window via notification window"""
        self.notification = error_code
        self.change_window("NotificationWindow")
    
    def call_success(self, success_code):
        """display success window via notification window"""
        self.notification = success_code
        self.undo()
        self.change_window("NotificationWindow")


class MainWindow(MenuWindow):
    """Start page, provides all user-necessary access"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            lds("Menu", "Меню"), 
            {lds("Mode selection", "Способы запоминать") : "ModeSelectionWindow", 
             lds("Create new card", "Создать новую карточку") : "CardCreationWindow",
             lds("Achievements", "Достижения") : "AchievementsWindow", 
             lds("Settings", "Настройки") : "SettingsWindow", 
             lds("Help", "Помощь") : "HelpWindow"}
        )
