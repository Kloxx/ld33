import sys, pygame
from DialogInterface import DialogInterface

size = width, height = 800, 600

def main(size):
    pygame.init()
    screen = pygame.display.set_mode(size)

    mainLoop(screen)

    pygame.quit()
    sys.exit()

def mainLoop(screen):
    endLoop = 0
    background = 0, 0, 255
    
    while not endLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endLoop = 1

#        screen.fill(background)
        testDialog = DialogInterface("test")
        testDialog.draw_portraits(screen)
        
        pygame.display.flip()


main(size)
