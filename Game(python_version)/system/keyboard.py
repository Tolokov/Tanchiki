import pygame
from os import environ


def controller(event, obj):
    # Up key
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        if environ['DEBUG'] == 'true':
            print('UP')
        obj.draw_rect(0, -1)

    # Down key
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        if environ['DEBUG'] == 'true':
            print('LEFT')
        obj.draw_rect(-1, 0)

    # Left key
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        if environ['DEBUG'] == 'true':
            print('DOWN')
        obj.draw_rect(0, 1)

    # Right key
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        if environ['DEBUG'] == 'true':
            print('RIGHT')
        obj.draw_rect(1, 0)

    # Shoot key
    elif event.key == pygame.K_SPACE or event.key == pygame.K_z:
        if environ['DEBUG'] == 'true':
            print('Z')

    # Pause key
    elif event.key == pygame.K_PAUSE:
        if environ['DEBUG'] == 'true':
            print('PAUSE')

    # Enter key
    elif event.key == pygame.K_RETURN:
        if environ['DEBUG'] == 'true':
            print('K_RETURN')
