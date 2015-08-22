import sys, pygame
import Input, Scene

size = width, height = 800, 600

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
    background = 0, 0, 0
    inputs = Input.Input()
    scene = Scene.Scene("scenes\scene1.txt")
    
    while not endLoop:
        startFrame = pygame.time.get_ticks()
        
        inputs.updateEvents()
        if inputs.quit == True:
            endLoop = 1
        if inputs.mouseButtons[0]:
            scene.setCharacterDest(inputs.getMousePos()[0])
        
        screen.fill(background)
        scene.drawScene(screen)
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

main(size)
