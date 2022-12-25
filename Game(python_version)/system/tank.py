import pygame
from os import environ


class Tank(object):
    def __init__(self, screen, display_size, bg_color):
        # Get window size
        self.border = display_size
        self.screen = screen
        self.bg_color = bg_color

        # Position
        self.pointX = 500
        self.pointY = 500
        self.wight = 50
        self.height = 50
        self.rectangle = pygame.draw.rect(self.screen, self.bg_color,
                                          (self.pointX, self.pointY, self.wight, self.height))
        self.speed = 25

        # Player image
        self.player_sprite_W = pygame.image.load(r"..\images\playerW.png").convert_alpha()
        self.player_sprite_W = pygame.transform.scale(self.player_sprite_W, (self.wight, self.height))

        self.player_sprite_A = pygame.image.load(r"..\images\playerA.png").convert_alpha()
        self.player_sprite_A = pygame.transform.scale(self.player_sprite_A, (self.wight, self.height))

        self.player_sprite_S = pygame.image.load(r"..\images\playerS.png").convert_alpha()
        self.player_sprite_S = pygame.transform.scale(self.player_sprite_S, (self.wight, self.height))

        self.player_sprite_D = pygame.image.load(r"..\images\playerD.png").convert_alpha()
        self.player_sprite_D = pygame.transform.scale(self.player_sprite_D, (self.wight, self.height))

        # Default direction
        self.player_sprite = self.player_sprite_W

        # Calculated border values
        self.head_border = self.border[0] - self.pointX
        self.foot_border = self.border[0] - self.pointX - self.height
        self.left_border = self.border[1] - self.pointY
        self.right_border = self.border[1] - self.pointY - self.wight

        # Draw player image
        self.screen.blit(self.player_sprite_W, self.rectangle)

    def draw_rect(self, x, y):
        move_x = x * self.speed
        move_y = y * self.speed

        # Find window borders
        self.left_border += move_x
        self.right_border -= move_x
        self.head_border += move_y
        self.foot_border -= move_y

        if environ['DEBUG'] == 'true':
            print(
                f'X={move_x} Y={move_y} '
                f'lb={self.left_border} rb={self.right_border} hb={self.head_border} fb={self.foot_border}'
            )

        if y == -1:
            self.player_sprite = self.player_sprite_W
        elif x == 1:
            self.player_sprite = self.player_sprite_D
        elif x == -1:
            self.player_sprite = self.player_sprite_A
        elif y == 1:
            self.player_sprite = self.player_sprite_S

        # IF a collision then stop
        if self.head_border < 0:
            move_x, move_y = 0, 0
            self.head_border = 0
            self.foot_border = self.border[0] - self.wight

        elif self.foot_border < 0:
            move_x, move_y = 0, 0
            self.foot_border = 0
            self.head_border = self.border[0] - self.wight

        elif self.right_border < 0:
            move_x, move_y = 0, 0
            self.right_border = 0
            self.left_border = self.border[1] - self.height

        elif self.left_border < 0:
            move_x, move_y = 0, 0
            self.left_border = 0
            self.right_border = self.border[1] - self.height

        self.rectangle = self.rectangle.move(move_x, move_y)
        pygame.draw.rect(self.screen, self.bg_color, self.rectangle)
        self.screen.blit(self.player_sprite, self.rectangle)

    def controller(self, event):
        # Up key
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            if environ['DEBUG'] == 'true':
                print('UP')
            self.draw_rect(0, -1)

        # Down key
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            if environ['DEBUG'] == 'true':
                print('LEFT')
            self.draw_rect(-1, 0)

        # Left key
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            if environ['DEBUG'] == 'true':
                print('DOWN')
            self.draw_rect(0, 1)

        # Right key
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            if environ['DEBUG'] == 'true':
                print('RIGHT')
            self.draw_rect(1, 0)

        # Shoot key
        elif event.key == pygame.K_SPACE or event.key == pygame.K_z:
            if environ['DEBUG'] == 'true':
                print('Z')
                self.draw_rect(0, 0)

        # Pause key
        elif event.key == pygame.K_PAUSE:
            if environ['DEBUG'] == 'true':
                print('PAUSE')
                self.draw_rect(0, 0)

        # Enter key
        elif event.key == pygame.K_RETURN:
            if environ['DEBUG'] == 'true':
                print('K_RETURN')
                self.draw_rect(0, 0)
        else:
            self.draw_rect(0, 0)
