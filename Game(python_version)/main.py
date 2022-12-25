import pygame
from os import environ

from system.tank import Tank
from system.objects import *

# Debug mod ON=true OFF=false
environ['DEBUG'] = 'true'


class GameWindow:
    def __init__(self):
        self.path_to_logo = '..\images\icon.png'
        self.display_size = (900, 900)
        self.background_color = (10, 10, 10)
        self.title = 'Tanchiki'
        self.status_run = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.screen = None
        self.objects = list()

    def set_icon(self):
        # Icon
        icon_img = pygame.image.load(self.path_to_logo)
        pygame.display.set_icon(icon_img)

    def create_window(self):
        # Display size and background color
        self.screen = pygame.display.set_mode(self.display_size)
        self.screen.fill(self.background_color)

        # Title and FLIP
        pygame.display.set_caption(self.title)
        pygame.display.flip()

    def build(self):
        # Infinite loop
        while self.status_run:
            for event in pygame.event.get():

                # Quit buttons
                if event.type == pygame.QUIT:
                    self.status_run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.status_run = False

                # Move buttons
                if event.type == pygame.KEYDOWN:
                    self.screen.fill(self.background_color)
                    self.player.controller(event)
                for obj in self.objects:
                    obj.draw_rect()
                if environ['DEBUG'] == 'true':
                    if pygame.mouse.get_focused():
                        pos = pygame.mouse.get_pos()
                        print(pos)

            # Display update
            pygame.display.update()
            self.clock.tick(self.fps)

    def run(self):
        # Window configure
        self.set_icon()
        self.create_window()
        self.screen = pygame.display.set_mode(self.display_size)
        self.screen.fill(self.background_color)

        # Game configure
        if environ['DEBUG'] == 'true':
            self.TEST_LEVEL()
        self.build()

    def create_player(self):
        self.player = Tank(self.screen, self.display_size, self.background_color)

    def create_wall(self, x, y):
        wall = Wall(self.screen, self.display_size, self.background_color, x, y)
        self.objects.append(wall)

    def create_tree(self, x, y):
        tree = Tree(self.screen, self.display_size, self.background_color, x, y)
        self.objects.append(tree)

    def create_water(self, x, y):
        water = Water(self.screen, self.display_size, self.background_color, x, y)
        self.objects.append(water)

    def create_base(self, x, y, destroy=False):
        base = Base(self.screen, self.display_size, self.background_color, x, y)
        self.objects.append(base)
        if destroy:
            base.destroy()

    def imp_wall(self, x, y):
        imp_wall = ImpenetrableWalls(self.screen, self.display_size, self.background_color, x, y)
        self.objects.append(imp_wall)

    def TEST_LEVEL(self):
        self.create_player()

        # Walls
        self.create_wall(x=250, y=400)
        self.create_wall(x=200, y=450)
        self.create_wall(x=250, y=450)
        self.create_wall(x=200, y=400)

        # Tree
        self.create_tree(x=650, y=400)
        self.create_tree(x=600, y=450)
        self.create_tree(x=650, y=450)
        self.create_tree(x=600, y=400)

        # Water
        self.create_water(x=250, y=600)
        self.create_water(x=200, y=650)
        self.create_water(x=250, y=650)
        self.create_water(x=200, y=600)

        # Base
        self.create_base(x=250, y=250)
        self.create_base(x=200, y=200, destroy=True)

        # Imp walls
        self.imp_wall(x=600, y=600)
        self.imp_wall(x=650, y=650)
        self.imp_wall(x=650, y=600)
        self.imp_wall(x=600, y=650)


if "__main__" == __name__:
    if environ['DEBUG'] == 'true':
        print('Debug mod: ON')
    game = GameWindow()
    game.run()
