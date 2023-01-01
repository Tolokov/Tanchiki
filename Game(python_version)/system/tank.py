from pygame import transform, image, draw
from pygame import K_LEFT, K_a, K_UP, K_w, K_DOWN, K_s, K_RIGHT, K_d, K_SPACE, K_z, K_PAUSE, K_RETURN
from os import environ
import time


class Bullet(object):
    def __init__(self):
        self.speed = 25
        self.direction = 'A'
        self.bullet_sprite = image.load(r"..\images\fireA.png").convert_alpha()
        self.bullet_sprite = transform.scale(self.bullet_sprite, (10, 10))


class Tank(object):
    def __init__(self, screen, display_size, bg_color, block_pixels, pointX, pointY):
        self.speed = 25

        # Get window size
        self.border = display_size
        self.screen = screen
        self.bg_color = bg_color
        self.bp = block_pixels
        self.pointX = pointX
        self.pointY = pointY

        # Position
        self.wight = 50
        self.height = 50
        self.rectangle = draw.rect(self.screen, self.bg_color, (self.pointX, self.pointY, self.wight, self.height))

        # Calculated border values
        self.head_border = self.pointY
        self.foot_border = self.border[1] - (self.wight + self.pointY)
        self.left_border = self.pointX
        self.right_border = self.border[0] - (self.wight + self.pointX)

        self.player_sprite = None
        self.player_sprite_W = None
        self.player_sprite_W_2 = None
        self.player_sprite_D = None
        self.player_sprite_D_2 = None
        self.player_sprite_A = None
        self.player_sprite_A_2 = None
        self.player_sprite_S = None
        self.player_sprite_S_2 = None

        self.w_animated = None
        self.a_animated = None
        self.d_animated = None
        self.s_animated = None

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

        draw.rect(self.screen, self.bg_color, self.rectangle)
        self.rectangle = self.rectangle.move(move_x, move_y)
        self.screen.blit(self.player_sprite, self.rectangle)

    @staticmethod
    def shot():
        print('SHOT!!!')
        Bullet()

    def get_bullet_pixels(self):
        return 'BULLET IS SHOT!!!!'



class Player(Tank):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.w_animated = True
        self.a_animated = True
        self.s_animated = True
        self.d_animated = True

        # Player images
        self.player_sprite_W = transform.scale(image.load(r"..\images\playerW.png"), (self.wight, self.height))
        self.player_sprite_W_2 = transform.scale(image.load(r"..\images\playerW1.png"), (self.wight, self.height))

        self.player_sprite_A = transform.scale(image.load(r"..\images\playerA.png"), (self.wight, self.height))
        self.player_sprite_A_2 = transform.scale(image.load(r"..\images\playerA1.png"), (self.wight, self.height))

        self.player_sprite_S = transform.scale(image.load(r"..\images\playerS.png"), (self.wight, self.height))
        self.player_sprite_S_2 = transform.scale(image.load(r"..\images\playerS1.png"), (self.wight, self.height))

        self.player_sprite_D = transform.scale(image.load(r"..\images\playerD.png"), (self.wight, self.height))
        self.player_sprite_D_2 = transform.scale(image.load(r"..\images\playerD1.png"), (self.wight, self.height))

        # Default direction
        self.player_sprite = self.player_sprite_W

        # Draw player image
        self.screen.blit(self.player_sprite_W, self.rectangle)

    def controller(self, event):
        # Up key
        if event.key == K_w or event.key == K_UP:
            if environ['DEBUG'] == 'true':
                print('UP ', end='')
            self.draw_rect(0, -1)

        # Down key
        elif event.key == K_a or event.key == K_LEFT:
            if environ['DEBUG'] == 'true':
                print('LEFT ', end='')
            self.draw_rect(-1, 0)

        # Left key
        elif event.key == K_s or event.key == K_DOWN:
            if environ['DEBUG'] == 'true':
                print('DOWN ', end='')
            self.draw_rect(0, 1)

        # Right key
        elif event.key == K_d or event.key == K_RIGHT:
            if environ['DEBUG'] == 'true':
                print('RIGHT ', end='')
            self.draw_rect(1, 0)

        # Shoot key
        elif event.key == K_SPACE or event.key == K_z:
            if environ['DEBUG'] == 'true':
                print('Z ', end='')
            self.draw_rect(0, 0)
            self.shot()

        # Pause key
        elif event.key == K_PAUSE:
            if environ['DEBUG'] == 'true':
                print('PAUSE ', end='')
            self.draw_rect(0, 0)

        # Enter key
        elif event.key == K_RETURN:
            if environ['DEBUG'] == 'true':
                print('K_RETURN ', end='')
            self.draw_rect(0, 0)
        else:
            self.draw_rect(0, 0)


class Enemy1(Tank):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.w_animated = True
        self.a_animated = True
        self.s_animated = True
        self.d_animated = True

        # Enemy images
        self.player_sprite_W = transform.scale(image.load(r"..\images\enemyW.png"), (self.wight, self.height))
        self.player_sprite_W_2 = transform.scale(image.load(r"..\images\enemyW1.png"), (self.wight, self.height))

        self.player_sprite_A = transform.scale(image.load(r"..\images\enemyA.png"), (self.wight, self.height))
        self.player_sprite_A_2 = transform.scale(image.load(r"..\images\enemyA1.png"), (self.wight, self.height))

        self.player_sprite_S = transform.scale(image.load(r"..\images\enemyS.png"), (self.wight, self.height))
        self.player_sprite_S_2 = transform.scale(image.load(r"..\images\enemyS1.png"), (self.wight, self.height))

        self.player_sprite_D = transform.scale(image.load(r"..\images\enemyD.png"), (self.wight, self.height))
        self.player_sprite_D_2 = transform.scale(image.load(r"..\images\enemyD1.png"), (self.wight, self.height))

        # Default direction
        self.player_sprite = self.player_sprite_W

        # Draw player image
        self.screen.blit(self.player_sprite_W, self.rectangle)

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


class Enemy2(Tank):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.w_animated = True
        self.a_animated = True
        self.s_animated = True
        self.d_animated = True

        # Player image
        self.player_sprite_W = transform.scale(image.load(r"..\images\green-enemyW.png"), (self.wight, self.height))
        self.player_sprite_W_2 = transform.scale(image.load(r"..\images\green-enemyW1.png"), (self.wight, self.height))

        self.player_sprite_A = transform.scale(image.load(r"..\images\green-enemyA.png"), (self.wight, self.height))
        self.player_sprite_A_2 = transform.scale(image.load(r"..\images\green-enemyA1.png"), (self.wight, self.height))

        self.player_sprite_S = transform.scale(image.load(r"..\images\green-enemyS.png"), (self.wight, self.height))
        self.player_sprite_S_2 = transform.scale(image.load(r"..\images\green-enemyS1.png"), (self.wight, self.height))

        self.player_sprite_D = transform.scale(image.load(r"..\images\green-enemyD.png"), (self.wight, self.height))
        self.player_sprite_D_2 = transform.scale(image.load(r"..\images\green-enemyD1.png"), (self.wight, self.height))

        # Default direction
        self.player_sprite = self.player_sprite_W

        # Draw player image
        self.screen.blit(self.player_sprite_W, self.rectangle)

    def controller(self):
        t = int(time.monotonic() + 1)
        if t % 5 == 0:
            self.draw_rect(-1, 0)
        elif t % 3 == 0:
            self.draw_rect(1, 0)
        elif t % 2 == 0:
            self.draw_rect(0, 1)
        else:
            self.draw_rect(0, -1)


class Enemy3(Tank):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.w_animated = True
        self.a_animated = True
        self.s_animated = True
        self.d_animated = True

        # Player image
        self.player_sprite_W = transform.scale(image.load(r"..\images\red-enemyW.png"), (self.wight, self.height))
        self.player_sprite_W_2 = transform.scale(image.load(r"..\images\red-enemyW1.png"), (self.wight, self.height))

        self.player_sprite_A = transform.scale(image.load(r"..\images\red-enemyA.png"), (self.wight, self.height))
        self.player_sprite_A_2 = transform.scale(image.load(r"..\images\red-enemyA1.png"), (self.wight, self.height))

        self.player_sprite_S = transform.scale(image.load(r"..\images\red-enemyS.png"), (self.wight, self.height))
        self.player_sprite_S_2 = transform.scale(image.load(r"..\images\red-enemyS1.png"), (self.wight, self.height))

        self.player_sprite_D = transform.scale(image.load(r"..\images\red-enemyD.png"), (self.wight, self.height))
        self.player_sprite_D_2 = transform.scale(image.load(r"..\images\red-enemyD1.png"), (self.wight, self.height))

        # Default direction
        self.player_sprite = self.player_sprite_W

        # Draw player image
        self.screen.blit(self.player_sprite_W, self.rectangle)

    def controller(self):
        t = int(time.monotonic() * 2)
        if t % 5 == 0:
            self.draw_rect(-1, 0)
        elif t % 3 == 0:
            self.draw_rect(1, 0)
        elif t % 2 == 0:
            self.draw_rect(0, 1)
        else:
            self.draw_rect(0, -1)
