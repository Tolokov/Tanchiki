import pygame

from system.keyboard import controller


class GameWindow:
    def __init__(self):
        self.path_to_logo = '..\images\icon.png'
        self.display_size = (1000, 1000)
        self.background_color = (105, 105, 105)
        self.title = 'Tanchiki'
        self.status_run = True

    def set_icon(self):
        icon_img = pygame.image.load(self.path_to_logo)
        pygame.display.set_icon(icon_img)

    def create_window(self):
        # display size and background color
        screen = pygame.display.set_mode(self.display_size)
        screen.fill(self.background_color)

        # Title and FLIP
        pygame.display.set_caption(self.title)
        pygame.display.flip()

    def build(self):
        while self.status_run:
            for event in pygame.event.get():

                # Quit buttons
                if event.type == pygame.QUIT:
                    self.status_run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.status_run = False

                # User action
                if event.type == pygame.KEYDOWN:
                    controller(event)

    def run(self):
        self.set_icon()
        self.create_window()
        self.build()


if "__main__" == __name__:
    game = GameWindow()
    game.run()
