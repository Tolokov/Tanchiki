import pygame


class Tank(object):
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.draw.rect(self.screen, (0, 0, 128), (500, 500, 16, 16))
        self.dist = 10

    def draw_rect(self, x, y):
        self.rect = self.rect.move(x*self.dist, y*self.dist)
        pygame.draw.rect(self.screen, (0, 0, 128), self.rect)

