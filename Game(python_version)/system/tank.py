import pygame


class Tank(object):
    def __init__(self, screen, display_size):
        self.border = display_size
        self.screen = screen

        self.pointX = 500
        self.pointY = 500
        self.wight = 50
        self.height = 50
        self.rectangle = pygame.draw.rect(self.screen, 'yellow', (self.pointX, self.pointY, self.wight, self.height))
        self.speed = 50

        self.head_border = self.border[0] - self.pointX
        self.foot_border = self.border[0] - self.pointX - self.height
        self.left_border = self.border[1] - self.pointY
        self.right_border = self.border[1] - self.pointY - self.wight

    def draw_rect(self, x, y):
        move_x = x * self.speed
        move_y = y * self.speed

        self.left_border += move_x
        self.right_border -= move_x
        self.head_border += move_y
        self.foot_border -= move_y

        if self.head_border < 0:
            move_x = 0
            move_y = 0
            self.head_border = 0
            self.foot_border = 950

        elif self.foot_border < 0:
            move_x = 0
            move_y = 0
            self.foot_border = 0
            self.head_border = 950

        elif self.right_border < 0:
            move_x = 0
            move_y = 0
            self.right_border = 0
            self.left_border = 950

        elif self.left_border < 0:
            move_x = 0
            move_y = 0
            self.left_border = 0
            self.right_border = 950

        self.rectangle = self.rectangle.move(move_x, move_y)
        pygame.draw.rect(self.screen, (255, 255, 0), self.rectangle)
