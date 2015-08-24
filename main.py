import sys, pygame
import Input, Scene, Map, Dialog

size = width, height = 800,500
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
                trigger = current.setCharacterDest(inputs.mouseX)
            if currentType == 1:
                trigger = current.isBoxClicked(inputs.getMousePos())
            if currentType == 2:
                trigger = current.getClickedRoom()
                print(trigger)
            pass
        if inputs.trigger:
            print('no error')

        if gameStart:
            print('intro')
            current = Map.Map()
            currentType = 2
            currentIndex = 0
            gameStart = False

        if trigger is not None:
            current, currentType, currentIndex, changeScreen = triggerManager(trigger, current, currentType, currentIndex)
            trigger = None
            
        if changeScreen:
            screen.fill(black)
            pygame.display.flip()
            pygame.time.delay(500)
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
    elif currentType == 1:
        if trigger == 0:
            if currentIndex == 4:
                print('load map')
                current = Map.Map()
                currentType = 2
                currentIndex = 0
                changeScreen = True
    elif currentType == 2:
        if trigger == 0:
            print('load walkway')
            current = Dialog.Dialog(size, "Dialogs/dialog_walkway1.txt")
            currentType = 1
            currentIndex = 4
            changeScreen = True
    return current, currentType, currentIndex, changeScreen

main(size)
