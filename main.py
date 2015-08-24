import sys, pygame
import Input, Scene, Map, Dialog

size = width, height = 800,500
def main(size):
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.event.set_blocked((pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION,
                             pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN))
    cursor = pygame.cursors.broken_x
    pygame.mouse.set_cursor(*cursor)

    mainLoop(screen)

    pygame.quit()
    sys.exit()


def mainLoop(screen):
    # pygame.mouse.set_cursor(*pygame.cursors.arrow)
    cursor = pygame.cursors.broken_x
    pygame.mouse.set_cursor(*cursor)
    frames = 0
    frameTime = 1000 / 60
    endLoop = 0
    background = 150, 150, 150
    black = 0, 0, 0
    inputs = Input.Input()
    #shipMap = Map.Map()
    #scene = Scene.Scene(size, "scenes/scene1.txt")
    #dialog = Dialog.Dialog(size, "Dialogs/dialog1.txt")
    gameStart = True
    trigger = None
    changeScreen = False
    
    while not endLoop:
        startFrame = pygame.time.get_ticks()

        # inputs
        inputs.updateEvents()
        if inputs.quit == True:
            endLoop = 1
        if inputs.mouseRelX or inputs.mouseRelY:
            if currentType == 2 or currentType == 0:
                current.isHovered(inputs.getMousePos())
            pass
        if inputs.mouseButtons[0]:
            if currentType == 0:
                # current.setCharacterDest(inputs.mouseX)
                current.onClick(inputs.mouseX)
            if currentType == 1:
                trigger = current.isBoxClicked(inputs.getMousePos())
            if currentType == 2:
                trigger = current.getClickedRoom()
                print(trigger)
            pass
        
        if inputs.trig:
            print('azeaze')
            print(inputs.trigger)

        if gameStart:
            current = Scene.Scene(size, "scenes/scene1.txt")
            currentType = 0
            currentIndex = 0
            gameStart = False

        if trigger is not None:
            current, currentType, currentIndex, changeScreen = triggerManager(trigger, current, currentType, currentIndex)
            trigger = None
            
        if changeScreen:
            screen.fill(black)
            pygame.display.flip()
            pygame.time.delay(1000)
            changeScreen = False
        
        screen.fill(background)
        current.draw(screen)
        #shipMap.draw(screen)
        #dialog.draw(screen)
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

def triggerManager(trigger, current, currentType, currentIndex):
    print('trigger : ', trigger)
    changeScreen = False
    if currentType == 0:
        pass
    if currentType == 1:
        pass
    if currentType == 2:
        if trigger == 0:
            current = Dialog.Dialog(size, "Dialogs/dialog1.txt")
            currentType = 1
            currentIndex = 0
            changeScreen = True
    return current, currentType, currentIndex, changeScreen

main(size)
