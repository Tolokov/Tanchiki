import pygame


class Barrier:
    def __init__(self, screen, display_size, bg_color, x, y):
        # Get window size
        self.border = display_size
        self.screen = screen
        self.bg_color = bg_color

        self.wight = 50
        self.height = 50
        self.pointX = x
        self.pointY = y

        self.rectangle = pygame.draw.rect(self.screen, self.bg_color,
                                          (self.pointX, self.pointY, self.wight, self.height))


class Wall(Barrier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hp = 1
        self.wall_sprite = pygame.image.load(r"..\images\bricks.png")
        self.wall_sprite = pygame.transform.scale(self.wall_sprite, (self.wight, self.height))

    def draw_rect(self):
        self.screen.blit(self.wall_sprite, self.rectangle)


class Tree(Barrier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wall_sprite = pygame.image.load(r"..\images\Tree.png").convert_alpha()
        self.wall_sprite = pygame.transform.scale(self.wall_sprite, (self.wight, self.height))

    def draw_rect(self):
        self.screen.blit(self.wall_sprite, self.rectangle)
