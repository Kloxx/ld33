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

        #other
        self.quit = False
        
    def updateEvents(self):
        self.mouseX = 0
        self.mouseY = 0
        self.mouseRelX = 0
        self.mouseRelY = 0
        
        for event in pygame.event.get():
            # mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseButtons[event.button] = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouseButtons[event.button] = False
            if event.type == pygame.MOUSEMOTION:
                self.mouseX, self.mouseY = event.pos
                self.mouseRelX, self.mouseRelY = event.rel

            # keyboard
            if event.type == pygame.KEYUP:
                self.keys[event.key] = True
            if event.type == pygame.KEYDOWN:
                self.keys[event.key] = False
				
	    #other
            if event.type == pygame.QUIT:
                self.quit = True
            
    def getKey(self, key):
        return self.keys[key]

    def getMouseButton(self, button):
        return self.mouseButtons[button]

    def getMousePos(self):
        return self.mouseX, self.mouseY

    def getMouseRel(self):
        return self.mouseRelX, self.mouseRelY

    def mouseMotion(self):
        return self.mouseRelX or self.mouseRelY