from .mode_windows import CARDS_ADVISE
from .windows import TextWindow
from .string_wrappers import LanguageDependentString as lds


class HelpWindow(TextWindow):
    """Provides user with necessary information about project"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            lds(("Press Esc to get back or close window "
                 "if there is nothing to return to\n"
                 "Press CTRL + BackSpace to close window\n"
                 "In classic cards window:\n"), 
                ("Нажмите Esc, чтобы вернуться назад или закрыть окно, "
                 "если некуда возвращаться\n"
                 "Нажмите CTRL + BackSpace, чтобы закрыть окно\n"
                 "В окне классических карточек:\n")) + CARDS_ADVISE
        )
