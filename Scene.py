import pygame
import Input

class Scene:
    def __init__(self, txtFile):
        var = None
        self.character = []
        self.characterPos = 100
        self.characterDest = 100
        self.characterFace = 1
        self.frame = 0
        txtFile = open(txtFile, "r")
        for line in txtFile.read().split("\n"):
            if line == "[background]":
                var = 0
                continue
            if line == "[character]":
                var = 1
                continue
            if line.startswith("["):
                var = None
            if line:
                if var == 0:
                    self.background = pygame.image.load(line)
                if var == 1:
                    self.character.append(pygame.image.load(line))
        txtFile.close()

    def drawScene(self, screen):
        # background
        screen.blit(self.background, (0,0))

        # character
        if self.frame < 20:
            i = 0
        elif self.frame < 40:
            i = 1
        else:
            i = 2
        self.setCharacterPos()
        if not self.characterFace:
            screen.blit(self.character[i], (self.characterPos, 300))
        if self.characterFace:
            screen.blit(pygame.transform.flip(self.character[i], 1, 0), (self.characterPos, 300))
        self.frame = (self.frame + 1) %60

    def setCharacterDest(self, pos):
        self.characterDest = pos

    def setCharacterPos(self):
        distance = self.characterDest - self.characterPos
        if distance >= 3:
            self.characterPos += 3
            self.characterFace = 1
        elif distance <= -3:
            self.characterPos -= 3
            self.characterFace = 0
        else:
            self.characterPos = self.characterDest
