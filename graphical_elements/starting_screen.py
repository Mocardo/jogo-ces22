from graphical_elements.button import Button


class StartingScreen:

    def __init__(self, screen):
        self.screen = screen
        self.play_button = Button(screen, "Play")

    def paint(self):
        self.play_button.draw_button()

    def check_if_started(self, mouse_x, mouse_y):
        return self.play_button.check_if_clicked(mouse_x, mouse_y)
