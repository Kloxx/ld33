import sys, pygame
import Input, Scene

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
    scene = Scene.Scene("scenes\scene1.txt")
    
    while not endLoop:        
        inputs.updateEvents()
        if inputs.quit == True or inputs.keys[pygame.K_ESCAPE] == True:
            endLoop = 1

        screen.fill(background)
        scene.drawScene(screen)
        pygame.display.flip()

main(size)
