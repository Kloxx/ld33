import pygame
import Input

class Scene:
    def __init__(self, txtFile):
        var = None
        self.character = []
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
        screen.blit(self.background, (0,0))
        if self.frame < 20:
            i = 0
        elif self.frame < 40:
            i = 1
        else:
            i = 2

        screen.blit(self.character[i], (200, 300))
        self.frame = (self.frame + 1) %60
