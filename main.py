import sys, pygame
import Input, Scene, Map, Dialog

size = width, height = 1600,1000

def main(size):
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.event.set_blocked((pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION,
                             pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN))

    mainLoop(screen)

    pygame.quit()
    sys.exit()


def mainLoop(screen):
    frames = 0
    frameTime = 1000 / 60
    endLoop = 0
    background = 150, 150, 150
    inputs = Input.Input()
    #shipMap = Map.Map()
    #scene = Scene.Scene(size, "scenes/scene1.txt")
    dialog = Dialog.Dialog(size, "Dialogs/dialog1.txt")
    
    while not endLoop:
        startFrame = pygame.time.get_ticks()
        
        inputs.updateEvents()
        if inputs.quit == True:
            endLoop = 1
        if inputs.mouseRelX or inputs.mouseRelY:
            #shipMap.isHovered(inputs.getMousePos())
            pass
        if inputs.mouseButtons[0]:
            pass
        
        screen.fill(background)
        #scene.draw(screen)
        #shipMap.draw(screen)
        dialog.draw(screen)
        pygame.display.flip()

        # manage framerate
        endFrame = pygame.time.get_ticks()
        loopTime = endFrame - startFrame
        if loopTime < frameTime:
            pygame.time.delay(frameTime - loopTime)
        frames += 1

    totalTime = pygame.time.get_ticks()
    avgFramerate = frames / (float(totalTime) / 1000)
    print("Frames : " + str(frames))
    print("Time Running : " + str(totalTime / 1000) + "s")
    print(avgFramerate)

def game(screen):
    pass
    

main(size)
