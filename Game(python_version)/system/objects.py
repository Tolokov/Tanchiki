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
        sprite = pygame.image.load(r"..\images\bricks.png")
        self.wall_sprite = pygame.transform.scale(sprite, (self.wight, self.height))

    def draw_rect(self):
        self.screen.blit(self.wall_sprite, self.rectangle)


class Tree(Barrier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sprite = pygame.image.load(r"..\images\Tree.png").convert_alpha()
        self.tree_sprite = pygame.transform.scale(sprite, (self.wight, self.height))

    def draw_rect(self):
        self.screen.blit(self.tree_sprite, self.rectangle)


class Water(Barrier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sprite = pygame.image.load(r"..\images\Water.png").convert_alpha()
        self.water_sprite = pygame.transform.scale(sprite, (self.wight, self.height))

    def draw_rect(self):
        self.screen.blit(self.water_sprite, self.rectangle)


class Base(Barrier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hp = 1
        sprite = pygame.image.load(r"..\images\base.png").convert_alpha()
        self.base_sprite = pygame.transform.scale(sprite, (self.wight, self.height))

    def draw_rect(self):
        self.screen.blit(self.base_sprite, self.rectangle)

    def destroy(self):
        sprite = pygame.image.load(r"..\images\base_des.png").convert_alpha()
        self.base_sprite = pygame.transform.scale(sprite, (self.wight, self.height))
        self.draw_rect()


class ImpenetrableWalls(Barrier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hp = 1
        sprite = pygame.image.load(r"..\images\Wall.png").convert_alpha()
        self.wall_sprite = pygame.transform.scale(sprite, (self.wight, self.height))

    def draw_rect(self):
        self.screen.blit(self.wall_sprite, self.rectangle)
