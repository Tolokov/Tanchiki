import pygame


def controller(event, obj):
    # Up key
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        print('UP')
        obj.draw_rect(0, -1)

    # Down key
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        print('LEFT')
        obj.draw_rect(-1, 0)

    # Left key
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        print('DOWN')
        obj.draw_rect(0, 1)

    # Right key
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        print('RIGHT')
        obj.draw_rect(1, 0)

    # Shoot key
    elif event.key == pygame.K_SPACE or event.key == pygame.K_z:
        print('Z')

    # Pause key
    elif event.key == pygame.K_PAUSE:
        print('PAUSE')

    # Enter key
    elif event.key == pygame.K_RETURN:
        print('K_RETURN')
