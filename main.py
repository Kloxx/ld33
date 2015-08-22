import sys, pygame
import Input

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
    inputs = Input.Input()
    
    while not endLoop:
        '''for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endLoop = 1'''
        
        inputs.updateEvents()
        if inputs.quit == True or inputs.keys[pygame.K_ESCAPE] == True:
            endLoop = 1

        screen.fill(background)
        pygame.display.flip()

main(size)
