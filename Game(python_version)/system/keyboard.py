import pygame


def controller(event):
    # Up key
    if event.key == pygame.K_w:
        print('w')
    elif event.key == pygame.K_UP:
        print('UP')

    # Down key
    elif event.key == pygame.K_a:
        print('a')
    elif event.key == pygame.K_LEFT:
        print('LEFT')

    # Left key
    elif event.key == pygame.K_s:
        print('s')
    elif event.key == pygame.K_DOWN:
        print('DOWN')

    # Right key
    elif event.key == pygame.K_d:
        print('d')
    elif event.key == pygame.K_RIGHT:
        print('RIGHT')

    # Shoot key
    elif event.key == pygame.K_SPACE:
        print('SPACE')
    elif event.key == pygame.K_z:
        print('Z')

    # Pause key
    elif event.key == pygame.K_PAUSE:
        print('PAUSE')

    # Enter key
    elif event.key == pygame.K_RETURN:
        print('K_RETURN')
