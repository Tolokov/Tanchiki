import pygame


def controller(event):

    if event.key == pygame.K_w:
        print('w')
    elif event.key == pygame.K_UP:
        print('UP')
    elif event.key == pygame.K_a:
        print('a')
    elif event.key == pygame.K_LEFT:
        print('LEFT')
    elif event.key == pygame.K_s:
        print('s')
    elif event.key == pygame.K_DOWN:
        print('DOWN')
    elif event.key == pygame.K_d:
        print('d')
    elif event.key == pygame.K_RIGHT:
        print('RIGHT')
    elif event.key == pygame.K_SPACE:
        print('SPACE')
