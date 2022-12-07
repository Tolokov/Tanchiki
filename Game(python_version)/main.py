import pygame


def main():
    # display size and background color
    screen = pygame.display.set_mode((1000, 1000))
    background_colour = (105, 105, 105)
    screen.fill(background_colour)

    # Title and FLIP
    pygame.display.set_caption('Tanchiki')
    pygame.display.flip()

    run = True
    while run:

        for event in pygame.event.get():

            # Quit buttons
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAP:
                run = False


if "__main__" == __name__:
    main()
