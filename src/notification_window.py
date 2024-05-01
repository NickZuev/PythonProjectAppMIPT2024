from .windows import TextWindow
from .string_wrappers import LanguageDependentString as lds


class NotificationWindow(TextWindow):
    """Resposible for handling all crucial raised exceptions"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            lds("How did you get here? None of exceptions was raised!",
                "Как ты сюда попал? Никаких же ошибок не произошло!")
        )
    
    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        self.label.config(
            text=self.controller.notification
        )
