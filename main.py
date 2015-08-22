import sys, pygame

size = width, height = 800, 600

def main(size):
    pygame.init()
    screen = pygame.display.set_mode(size)

    mainLoop(screen)

    pygame.quit()
    sys.exit()


def mainLoop(screen):
    endLoop = 0
    background = 0, 0, 0
    print(pygame.K_ESCAPE)
    
    while not endLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endLoop = 1
            if pygame.key.get_mods() == 27:
                endLoop = 1

        screen.fill(background)
        pygame.display.flip()

main(size)
