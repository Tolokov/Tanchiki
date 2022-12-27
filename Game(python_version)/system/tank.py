import pygame
from os import environ
import time


class Tank(object):
    def __init__(self, screen, display_size, bg_color, block_pixels):
        # Get window size
        self.border = display_size
        self.screen = screen
        self.bg_color = bg_color
        self.bp = block_pixels

        # Position
        self.pointX = int(display_size[0] / 2)
        self.pointY = int(display_size[0] / 2)
        self.wight = 50
        self.height = 50
        self.rectangle = pygame.draw.rect(self.screen, self.bg_color,
                                          (self.pointX, self.pointY, self.wight, self.height))
        self.speed = 25

        # Player image
        self.player_sprite_W = pygame.image.load(r"..\images\playerW.png").convert_alpha()
        self.player_sprite_W = pygame.transform.scale(self.player_sprite_W, (self.wight, self.height))
        self.w_animated = True
        self.player_sprite_W_2 = pygame.image.load(r"..\images\playerW1.png").convert_alpha()
        self.player_sprite_W_2 = pygame.transform.scale(self.player_sprite_W_2, (self.wight, self.height))

        self.player_sprite_A = pygame.image.load(r"..\images\playerA.png").convert_alpha()
        self.player_sprite_A = pygame.transform.scale(self.player_sprite_A, (self.wight, self.height))
        self.a_animated = True
        self.player_sprite_A_2 = pygame.image.load(r"..\images\playerA1.png").convert_alpha()
        self.player_sprite_A_2 = pygame.transform.scale(self.player_sprite_A_2, (self.wight, self.height))

        self.player_sprite_S = pygame.image.load(r"..\images\playerS.png").convert_alpha()
        self.player_sprite_S = pygame.transform.scale(self.player_sprite_S, (self.wight, self.height))
        self.s_animated = True
        self.player_sprite_S_2 = pygame.image.load(r"..\images\playerS1.png").convert_alpha()
        self.player_sprite_S_2 = pygame.transform.scale(self.player_sprite_S_2, (self.wight, self.height))

        self.player_sprite_D = pygame.image.load(r"..\images\playerD.png").convert_alpha()
        self.player_sprite_D = pygame.transform.scale(self.player_sprite_D, (self.wight, self.height))
        self.d_animated = True
        self.player_sprite_D_2 = pygame.image.load(r"..\images\playerD1.png").convert_alpha()
        self.player_sprite_D_2 = pygame.transform.scale(self.player_sprite_D_2, (self.wight, self.height))

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
        temp_left_border = self.left_border
        temp_head_border = self.head_border
        temp_right_border = self.right_border
        temp_foot_border = self.foot_border

        # Border calculate
        self.left_border += move_x
        self.right_border -= move_x
        self.head_border += move_y
        self.foot_border -= move_y

        # if environ['DEBUG'] == 'true':
        # print(
        #     f'X={move_x} Y={move_y} '
        #     f'lb={self.left_border} rb={self.right_border} hb={self.head_border} fb={self.foot_border}'
        # )

        def return_self_borders():
            self.left_border = temp_left_border
            self.head_border = temp_head_border
            self.right_border = temp_right_border
            self.foot_border = temp_foot_border

        # Collision
        if y == -1:
            if self.w_animated:
                self.player_sprite = self.player_sprite_W
                self.w_animated = False
            else:
                self.player_sprite = self.player_sprite_W_2
                self.w_animated = True

            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border - 25 == i and self.head_border - 25 == j) \
                        or (self.left_border == i and self.head_border - 25 == j) \
                        or (self.left_border + 25 == i and self.head_border - 25 == j):
                    move_y = 0
                    return_self_borders()

        elif x == 1:
            if self.d_animated:
                self.player_sprite = self.player_sprite_D
                self.d_animated = False
            else:
                self.player_sprite = self.player_sprite_D_2
                self.d_animated = True
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border + 25 == i and self.head_border == j) \
                        or (self.left_border + 25 == i and self.head_border + 25 == j) or \
                        (self.left_border + 25 == i and self.head_border - 25) == j:
                    move_x = 0
                    return_self_borders()

        elif x == -1:
            if self.a_animated:
                self.player_sprite = self.player_sprite_A
                self.a_animated = False
            else:
                self.player_sprite = self.player_sprite_A_2
                self.a_animated = True
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border - 25 == i and self.head_border == j) \
                        or (self.left_border - 25 == i and self.head_border - 25 == j) or \
                        (self.left_border - 25 == i and self.head_border + 25) == j:
                    move_x = 0
                    return_self_borders()

        elif y == 1:
            if self.s_animated:
                self.player_sprite = self.player_sprite_S
                self.s_animated = False
            else:
                self.player_sprite = self.player_sprite_S_2
                self.s_animated = True
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border - 25 == i and self.head_border + 25 == j) \
                        or (self.left_border == i and self.head_border + 25 == j) \
                        or (self.left_border + 25 == i and self.head_border + 25 == j):
                    move_y = 0
                    return_self_borders()

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
            # if environ['DEBUG'] == 'true':
            #     print('UP')
            self.draw_rect(0, -1)

        # Down key
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            # if environ['DEBUG'] == 'true':
            #     print('LEFT')
            self.draw_rect(-1, 0)

        # Left key
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            # if environ['DEBUG'] == 'true':
            #     print('DOWN')
            self.draw_rect(0, 1)

        # Right key
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            # if environ['DEBUG'] == 'true':
            #     print('RIGHT')
            self.draw_rect(1, 0)

        # Shoot key
        elif event.key == pygame.K_SPACE or event.key == pygame.K_z:
            # if environ['DEBUG'] == 'true':
            #     print('Z')
            self.draw_rect(0, 0)

        # Pause key
        elif event.key == pygame.K_PAUSE:
            # if environ['DEBUG'] == 'true':
            #     print('PAUSE')
            self.draw_rect(0, 0)

        # Enter key
        elif event.key == pygame.K_RETURN:
            # if environ['DEBUG'] == 'true':
            #     print('K_RETURN')
            self.draw_rect(0, 0)
        else:
            self.draw_rect(0, 0)


class Enemy_1:
    def __init__(self, screen, display_size, bg_color, block_pixels, pointX, pointY):
        # Get window size
        self.border = display_size
        self.screen = screen
        self.bg_color = bg_color
        self.bp = block_pixels

        # Position
        self.pointX = pointX
        self.pointY = pointY
        self.wight = 50
        self.height = 50
        self.rectangle = pygame.draw.rect(self.screen, self.bg_color,
                                          (self.pointX, self.pointY, self.wight, self.height))
        self.speed = 25

        # Player image
        self.player_sprite_W = pygame.image.load(r"..\images\playerW.png").convert_alpha()
        self.player_sprite_W = pygame.transform.scale(self.player_sprite_W, (self.wight, self.height))
        self.w_animated = True
        self.player_sprite_W_2 = pygame.image.load(r"..\images\playerW1.png").convert_alpha()
        self.player_sprite_W_2 = pygame.transform.scale(self.player_sprite_W_2, (self.wight, self.height))

        self.player_sprite_A = pygame.image.load(r"..\images\playerA.png").convert_alpha()
        self.player_sprite_A = pygame.transform.scale(self.player_sprite_A, (self.wight, self.height))
        self.a_animated = True
        self.player_sprite_A_2 = pygame.image.load(r"..\images\playerA1.png").convert_alpha()
        self.player_sprite_A_2 = pygame.transform.scale(self.player_sprite_A_2, (self.wight, self.height))

        self.player_sprite_S = pygame.image.load(r"..\images\playerS.png").convert_alpha()
        self.player_sprite_S = pygame.transform.scale(self.player_sprite_S, (self.wight, self.height))
        self.s_animated = True
        self.player_sprite_S_2 = pygame.image.load(r"..\images\playerS1.png").convert_alpha()
        self.player_sprite_S_2 = pygame.transform.scale(self.player_sprite_S_2, (self.wight, self.height))

        self.player_sprite_D = pygame.image.load(r"..\images\playerD.png").convert_alpha()
        self.player_sprite_D = pygame.transform.scale(self.player_sprite_D, (self.wight, self.height))
        self.d_animated = True
        self.player_sprite_D_2 = pygame.image.load(r"..\images\playerD1.png").convert_alpha()
        self.player_sprite_D_2 = pygame.transform.scale(self.player_sprite_D_2, (self.wight, self.height))

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
        temp_left_border = self.left_border
        temp_head_border = self.head_border
        temp_right_border = self.right_border
        temp_foot_border = self.foot_border

        # Border calculate
        self.left_border += move_x
        self.right_border -= move_x
        self.head_border += move_y
        self.foot_border -= move_y

        def return_self_borders():
            self.left_border = temp_left_border
            self.head_border = temp_head_border
            self.right_border = temp_right_border
            self.foot_border = temp_foot_border

        # Collision
        if y == -1:
            self.player_sprite = self.player_sprite_W
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border - 25 == i and self.head_border - 25 == j) \
                        or (self.left_border == i and self.head_border - 25 == j) \
                        or (self.left_border + 25 == i and self.head_border - 25 == j):
                    move_y = 0
                    return_self_borders()

        elif x == 1:
            self.player_sprite = self.player_sprite_D
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border + 25 == i and self.head_border == j) \
                        or (self.left_border + 25 == i and self.head_border + 25 == j) or \
                        (self.left_border + 25 == i and self.head_border - 25) == j:
                    move_x = 0
                    return_self_borders()

        elif x == -1:
            self.player_sprite = self.player_sprite_A
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border - 25 == i and self.head_border == j) \
                        or (self.left_border - 25 == i and self.head_border - 25 == j) or \
                        (self.left_border - 25 == i and self.head_border + 25) == j:
                    move_x = 0
                    return_self_borders()

        elif y == 1:
            self.player_sprite = self.player_sprite_S
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border - 25 == i and self.head_border + 25 == j) \
                        or (self.left_border == i and self.head_border + 25 == j) \
                        or (self.left_border + 25 == i and self.head_border + 25 == j):
                    move_y = 0
                    return_self_borders()

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

    def controller(self):
        t = int(time.monotonic())
        if t % 5 == 0:
            self.draw_rect(-1, 0)
        elif t % 3 == 0:
            self.draw_rect(1, 0)
        elif t % 2 == 0:
            self.draw_rect(0, 1)
        else:
            self.draw_rect(0, -1)


class Enemy_2:
    def __init__(self, screen, display_size, bg_color, block_pixels, pointX, pointY):
        # Get window size
        self.border = display_size
        self.screen = screen
        self.bg_color = bg_color
        self.bp = block_pixels

        # Position
        self.pointX = pointX
        self.pointY = pointY
        self.wight = 50
        self.height = 50
        self.rectangle = pygame.draw.rect(self.screen, self.bg_color,
                                          (self.pointX, self.pointY, self.wight, self.height))
        self.speed = 25

        # Player image
        self.player_sprite_W = pygame.image.load(r"..\images\playerW.png").convert_alpha()
        self.player_sprite_W = pygame.transform.scale(self.player_sprite_W, (self.wight, self.height))
        self.w_animated = True
        self.player_sprite_W_2 = pygame.image.load(r"..\images\playerW1.png").convert_alpha()
        self.player_sprite_W_2 = pygame.transform.scale(self.player_sprite_W_2, (self.wight, self.height))

        self.player_sprite_A = pygame.image.load(r"..\images\playerA.png").convert_alpha()
        self.player_sprite_A = pygame.transform.scale(self.player_sprite_A, (self.wight, self.height))
        self.a_animated = True
        self.player_sprite_A_2 = pygame.image.load(r"..\images\playerA1.png").convert_alpha()
        self.player_sprite_A_2 = pygame.transform.scale(self.player_sprite_A_2, (self.wight, self.height))

        self.player_sprite_S = pygame.image.load(r"..\images\playerS.png").convert_alpha()
        self.player_sprite_S = pygame.transform.scale(self.player_sprite_S, (self.wight, self.height))
        self.s_animated = True
        self.player_sprite_S_2 = pygame.image.load(r"..\images\playerS1.png").convert_alpha()
        self.player_sprite_S_2 = pygame.transform.scale(self.player_sprite_S_2, (self.wight, self.height))

        self.player_sprite_D = pygame.image.load(r"..\images\playerD.png").convert_alpha()
        self.player_sprite_D = pygame.transform.scale(self.player_sprite_D, (self.wight, self.height))
        self.d_animated = True
        self.player_sprite_D_2 = pygame.image.load(r"..\images\playerD1.png").convert_alpha()
        self.player_sprite_D_2 = pygame.transform.scale(self.player_sprite_D_2, (self.wight, self.height))

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
        temp_left_border = self.left_border
        temp_head_border = self.head_border
        temp_right_border = self.right_border
        temp_foot_border = self.foot_border

        # Border calculate
        self.left_border += move_x
        self.right_border -= move_x
        self.head_border += move_y
        self.foot_border -= move_y

        def return_self_borders():
            self.left_border = temp_left_border
            self.head_border = temp_head_border
            self.right_border = temp_right_border
            self.foot_border = temp_foot_border

        # Collision
        if y == -1:
            self.player_sprite = self.player_sprite_W
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border - 25 == i and self.head_border - 25 == j) \
                        or (self.left_border == i and self.head_border - 25 == j) \
                        or (self.left_border + 25 == i and self.head_border - 25 == j):
                    move_y = 0
                    return_self_borders()

        elif x == 1:
            self.player_sprite = self.player_sprite_D
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border + 25 == i and self.head_border == j) \
                        or (self.left_border + 25 == i and self.head_border + 25 == j) or \
                        (self.left_border + 25 == i and self.head_border - 25) == j:
                    move_x = 0
                    return_self_borders()

        elif x == -1:
            self.player_sprite = self.player_sprite_A
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border - 25 == i and self.head_border == j) \
                        or (self.left_border - 25 == i and self.head_border - 25 == j) or \
                        (self.left_border - 25 == i and self.head_border + 25) == j:
                    move_x = 0
                    return_self_borders()

        elif y == 1:
            self.player_sprite = self.player_sprite_S
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border - 25 == i and self.head_border + 25 == j) \
                        or (self.left_border == i and self.head_border + 25 == j) \
                        or (self.left_border + 25 == i and self.head_border + 25 == j):
                    move_y = 0
                    return_self_borders()

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

    def controller(self):
        t = int(time.monotonic())
        if t % 5 == 0:
            self.draw_rect(-1, 0)
        elif t % 3 == 0:
            self.draw_rect(1, 0)
        elif t % 2 == 0:
            self.draw_rect(0, 1)
        else:
            self.draw_rect(0, -1)


class Enemy_3:
    def __init__(self, screen, display_size, bg_color, block_pixels, pointX, pointY):
        # Get window size
        self.border = display_size
        self.screen = screen
        self.bg_color = bg_color
        self.bp = block_pixels

        # Position
        self.pointX = pointX
        self.pointY = pointY
        self.wight = 50
        self.height = 50
        self.rectangle = pygame.draw.rect(self.screen, self.bg_color,
                                          (self.pointX, self.pointY, self.wight, self.height))
        self.speed = 25

        # Player image
        self.player_sprite_W = pygame.image.load(r"..\images\playerW.png").convert_alpha()
        self.player_sprite_W = pygame.transform.scale(self.player_sprite_W, (self.wight, self.height))
        self.w_animated = True
        self.player_sprite_W_2 = pygame.image.load(r"..\images\playerW1.png").convert_alpha()
        self.player_sprite_W_2 = pygame.transform.scale(self.player_sprite_W_2, (self.wight, self.height))

        self.player_sprite_A = pygame.image.load(r"..\images\playerA.png").convert_alpha()
        self.player_sprite_A = pygame.transform.scale(self.player_sprite_A, (self.wight, self.height))
        self.a_animated = True
        self.player_sprite_A_2 = pygame.image.load(r"..\images\playerA1.png").convert_alpha()
        self.player_sprite_A_2 = pygame.transform.scale(self.player_sprite_A_2, (self.wight, self.height))

        self.player_sprite_S = pygame.image.load(r"..\images\playerS.png").convert_alpha()
        self.player_sprite_S = pygame.transform.scale(self.player_sprite_S, (self.wight, self.height))
        self.s_animated = True
        self.player_sprite_S_2 = pygame.image.load(r"..\images\playerS1.png").convert_alpha()
        self.player_sprite_S_2 = pygame.transform.scale(self.player_sprite_S_2, (self.wight, self.height))

        self.player_sprite_D = pygame.image.load(r"..\images\playerD.png").convert_alpha()
        self.player_sprite_D = pygame.transform.scale(self.player_sprite_D, (self.wight, self.height))
        self.d_animated = True
        self.player_sprite_D_2 = pygame.image.load(r"..\images\playerD1.png").convert_alpha()
        self.player_sprite_D_2 = pygame.transform.scale(self.player_sprite_D_2, (self.wight, self.height))

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
        temp_left_border = self.left_border
        temp_head_border = self.head_border
        temp_right_border = self.right_border
        temp_foot_border = self.foot_border

        # Border calculate
        self.left_border += move_x
        self.right_border -= move_x
        self.head_border += move_y
        self.foot_border -= move_y

        def return_self_borders():
            self.left_border = temp_left_border
            self.head_border = temp_head_border
            self.right_border = temp_right_border
            self.foot_border = temp_foot_border

        # Collision
        if y == -1:
            self.player_sprite = self.player_sprite_W
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border - 25 == i and self.head_border - 25 == j) \
                        or (self.left_border == i and self.head_border - 25 == j) \
                        or (self.left_border + 25 == i and self.head_border - 25 == j):
                    move_y = 0
                    return_self_borders()

        elif x == 1:
            self.player_sprite = self.player_sprite_D
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border + 25 == i and self.head_border == j) \
                        or (self.left_border + 25 == i and self.head_border + 25 == j) or \
                        (self.left_border + 25 == i and self.head_border - 25) == j:
                    move_x = 0
                    return_self_borders()

        elif x == -1:
            self.player_sprite = self.player_sprite_A
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border - 25 == i and self.head_border == j) \
                        or (self.left_border - 25 == i and self.head_border - 25 == j) or \
                        (self.left_border - 25 == i and self.head_border + 25) == j:
                    move_x = 0
                    return_self_borders()

        elif y == 1:
            self.player_sprite = self.player_sprite_S
            for i, j, k, l in self.bp:
                # print(i, j, k, l)
                if (self.left_border - 25 == i and self.head_border + 25 == j) \
                        or (self.left_border == i and self.head_border + 25 == j) \
                        or (self.left_border + 25 == i and self.head_border + 25 == j):
                    move_y = 0
                    return_self_borders()

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

    def controller(self):
        t = int(time.monotonic())
        if t % 5 == 0:
            self.draw_rect(-1, 0)
        elif t % 3 == 0:
            self.draw_rect(1, 0)
        elif t % 2 == 0:
            self.draw_rect(0, 1)
        else:
            self.draw_rect(0, -1)
