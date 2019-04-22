from graphical_elements.button import Button


class StartingScreen:
    play_button = None

    def __init__(self, screen):
        self.screen = screen
        self.__class__.play_button = Button(screen, "Play")

    def paint(self):
        pass # TODO