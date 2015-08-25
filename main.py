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
    isTriggered = [0,0,0,0,0,0,0,0] # global vars
    
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
                current.onClick(inputs.mouseX)
            if currentType == 1:
                trigger = current.isBoxClicked(inputs.getMousePos())
            if currentType == 2:
                trigger = current.getClickedRoom()
            if currentType == 3:
                trigger = 0
                
        if inputs.trig:
            trigger = inputs.trigger

        if gameStart:
            print('intro')
            current = Dialog.Dialog2(size, "Dialogs/dialog_intro.txt")
            currentType = 3
            currentIndex = 2
            gameStart = False

        if trigger is not None:
            changeState = None
            current, currentType, currentIndex, changeScreen, changeState = triggerManager(trigger, current, currentType, currentIndex, isTriggered)
            if changeState is not None:
                isTriggered[changeState] = 1
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

def triggerManager(trigger, current, currentType, currentIndex, isTriggered):
    changeScreen = False
    changeState = None
    # scenes
    if currentType == 0:
        if currentIndex == 2:
            # lab
            current.displayComment(trigger)
            if trigger == 0 and not isTriggered[0]: # box
                changeState = 0
                current = Scene.Scene(size, "scenes/scene_lab2.txt")
                currentType = 0
                currentIndex = 2
                changeScreen = True
            if trigger == 1: # switch
                changeState = 1
            if trigger == 2: # door
                if isTriggered[0] and isTriggered[1]:
                    # -> dialog guard1
                    current = Dialog.Dialog(size, "dialogs/dialog_walkway1.txt")
                    currentType = 1
                    currentIndex = 4
                    changeScreen = True
                elif isTriggered[0] or not(isTriggered[0] and isTriggered[1]): # ferme
                    pass
                elif isTriggered[1]: # ouvert, mais...
                    pass
        if currentIndex == 5:
            # cantina
            if trigger == 0: # cook
                # -> dialog cook
                current = Dialog.Dialog(size, "dialogs/dialog_cantina1.txt")
                currentType = 1
                currentIndex = 6
                changeScreen = True
        if currentIndex == 10:
            # mainframe
            if trigger == 0: # guard2
                # -> dialog guard2
                current = Dialog.Dialog(size, "dialogs/dialog_mainframe1.txt")
                currentType = 1
                currentIndex = 8
                changeScreen = True
            if trigger == 1: # computer
                # -> dialog computer
                current = Dialog.Dialog(size, "dialogs/dialog_mainframe2.txt")
                currentType = 1
                currentIndex = 9
                changeScreen = True
        if currentIndex == 12:
            # deck
            if trigger == 0: # navigator
                current = Dialog.Dialog(size, "dialogs/dialog_flightdeck1.txt")
                currentType = 1
                currentIndex = 11
                changeScreen = True             
                

    # dialogs
    elif currentType == 1:
        if trigger == 0:
            if currentIndex == 4:
                # end guard1 -> map
                current = Map.Map(size)
                currentType = 2
                currentIndex = 0
                changeScreen = True
                changeState = 2
            if currentIndex == 6:
                # end cook -> cantina
                current = Scene.Scene(size, "scenes/scene_cantina1.txt")
                currentType = 0
                currentIndex = 5
                changeScreen = True
                changeState = 3
            if currentIndex == 8:
                # end guard2 -> mainframe
                current = Scene.Scene(size, "scenes/scene_mainframe1.txt")
                currentType = 0
                currentIndex = 10
                changeScreen = True
                changeState = 5
            if currentIndex == 9:
                # end computer -> mainframe
                current = Scene.Scene(size, "scenes/scene_mainframe1.txt")
                currentType = 0
                currentIndex = 10
                changeScreen = True
                changeState = 6
            if currentIndex == 11:
                # end navigator -> deck
                current = Scene.Scene(size, "scenes/scene_flightdeck1.txt")
                currentType = 0
                currentIndex = 12
                changeScreen = True
                changeState = 7

    # map
    elif currentType == 2:
        if trigger == 0: # cantina
            current = Scene.Scene(size, "scenes/scene_cantina1.txt")
            currentType = 0
            currentIndex = 5
            changeScreen = True
        if trigger == 1: # labo
            current = Scene.Scene(size, "scenes/scene_lab2.txt")
            currentType = 0
            currentIndex = 2
            changeScreen = True
        if trigger == 2: # deck
            current = Scene.Scene(size, "scenes/scene_flightdeck1.txt")
            currentType = 0
            currentIIndex = 12
            changeScreen = True
        if trigger == 3: # mainframe
            current = Scene.Scene(size, "scenes/scene_mainframe1.txt")
            currentType = 0
            currentIndex = 10
            changeScreen = True
        if trigger == 4: # walkway
            pass

    # auto-dialogs
    elif currentType == 3:
        trigger = current.nextSentence()
        if trigger:
            current = Scene.Scene(size, "scenes/scene_lab1.txt")
            currentType = 0
            currentIndex = 2
            changeScreen = True
    return current, currentType, currentIndex, changeScreen, changeState

main(size)
