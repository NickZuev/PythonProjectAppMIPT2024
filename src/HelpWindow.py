from Cards import CARDS_ADVISE
from WindowFactory import WindowsFactory


class HelpWindow(WindowsFactory):
    """Provides user with necessary information about project"""
    def __init__(self, parent, controller):
        super().__init__(
            parent, 
            controller, 
            """This is the help page
            Press Esc to return to Menu
            Go on Cards window and """ + CARDS_ADVISE
        )
