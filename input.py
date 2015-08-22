import pygame

class Input:
    """ Manager for keyboard and mouse inputs and motion """

    def __init__(self):
        # mouse
        self.mouseX = 0
        self.mouseY = 0
        self.mouseRelX = 0
        self.mouseRelY = 0
        self.mouseButtons = []
        self.keys = []
        for i in range(0, 3):
            self.mouseButtons.append(False)

        # keyboard
        for i in range(0, 134):
            self.keys.append(False)
        
    def updateEvents():
        self.mouseX = 0
        self.mouseY = 0
        self.mouseRelX = 0
        self.mouseRelY = 0
        
        for event in pygame.event.get():
            # mouse
            if event.type == MOUSEBUTTONDOWN:
                self.mouseButtons[event.button] = True
            if event.type == MOUSEBUTTONUP:
                self.mouseButtons[event.button] = False
            if event.type == MOUSEMOTION:
                self.mouseX, self.mouseY = event.pos
                self.mouseRelX, self.mouseRelY = event.rel

            # keyboard
            if event.type == KEYUP:
                self.keys[event.key] = True
            if event.type == KEYDOWN:
                self.keys[event.key] = False
            
    def getKey(key):
        return self.keys[key]

    def getMouseButton(button):
        return self.mouseButtons[button]

    def getMousePos():
        return self.mouseX, self.mouseY

    def getMouseRel():
        return self.mouseRelX, self.mouseRelY

    def mouseMotion():
        return self.mouseRelX or self.mouseRelY
