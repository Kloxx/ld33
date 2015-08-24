import pygame
import Input

class Map:
    def __init__(self, size):
        self.size = size
        self.mapSurface = pygame.transform.scale(pygame.image.load("assets/map/map.png").convert_alpha(), self.size)
        txtFile = open("assets/map/map.txt", "r")
        var = None
        self.coordinates = []
        self.roomRects = []
        self.isRoomHovered = []
        for line in txtFile.read().split("\n"):
            if line == "[cafeteria]":
                var = 0
                self.coordinates.append([])
                continue
            if line == "[labo]":
                var = 1
                self.coordinates.append([])
                continue
            if line == "[deck]":
                var = 2
                self.coordinates.append([])
                continue
            if line == "[mainframe]":
                var = 3
                self.coordinates.append([])
                continue
            if line == "[walkway]":
                var = 4
                self.coordinates.append([])
                continue
            if line:
                x,y,w,h = line.split(",")
                x,y,w,h = int(x), int(y), int(w), int(h)
                x,y,w,h = x*self.size[0]/800, y*self.size[1]/600, w*self.size[0]/800, h*self.size[1]/600
                self.roomRects.append(pygame.Rect(x,y,w,h))
                self.isRoomHovered.append(False)

    def draw(self, screen):
        for index, room in enumerate(self.roomRects):
            if self.isRoomHovered[index]:
                pygame.draw.rect(screen, (255,255,255), self.roomRects[index])
        screen.blit(self.mapSurface, (0,0))

    def isHovered(self, pos):
        for index, room in enumerate(self.roomRects):
            self.isRoomHovered[index] = room.collidepoint(pos)

    def getClickedRoom(self):
        for index, room in enumerate(self.isRoomHovered):
            if room:
                return index
        return None
