import pygame
import Input

class Map:
    def __init__(self):
        self.mapSurface = pygame.image.load("assets/map/map.png").convert_alpha()
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
            if line == "[pont]":
                var = 2
                self.coordinates.append([])
                continue
            if line == "[ordi]":
                var = 3
                self.coordinates.append([])
                continue
            if line:
                x,y = line.split(",")
                self.coordinates[var].append((int(x),int(y)))
                self.isRoomHovered.append(False)
        for coord in self.coordinates:
            self.roomRects.append(pygame.Rect(coord[0],coord[2]))

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
