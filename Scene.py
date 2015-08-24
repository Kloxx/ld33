import pygame
import Input

class Scene:
    def __init__(self, size, txtFile):
        self.character = []
        self.background = None
        self.characterPos = 100
        self.characterDest = 100
        self.characterFace = 1
        self.frame = 0
        self.size = size
        self.pos = (0,0)
        var = 0
        self.objectFont = pygame.font.Font(None, 36)
        self.objectNames = []
        self.objectRects = []
        self.objectComments = []
        self.objectCommentCount = []
        self.isObjectHovered = []
        self.trigger = None
        self.showComment = False
        self.commentText = None

        self.loadAssets(txtFile)

    def loadAssets(self, txtFile):
        var = None
        txtFile = open(txtFile, "r")
        for line in txtFile.read().split("\n"):
            if line == "[background]":
                var = 0
                continue
            if line == "[character]":
                var = 1
                continue
            if line == "[objects]":
                var = 2
                continue
            if line.startswith("["):
                var = None
                break
            if line:
                if var == 0:
                    self.background = pygame.transform.scale(pygame.image.load(line).convert(), self.size)
                if var == 1:
                    self.character.append(pygame.image.load(line).convert_alpha())
                if var == 2:
                    name = line.split(":")[0]
                    coord = line.split(":")[1]
                    comments = line.split(":")[2:]
                    x,y,w,h = coord.split(",")
                    x,y,w,h = int(x), int(y), int(w), int(h)
                    self.objectNames.append(name)
                    self.isObjectHovered.append(False)
                    self.objectRects.append(pygame.Rect(x,y,w,h))
                    temp = []
                    for comment in comments:
                        if comment:
                            temp.append(comment)
                    self.objectComments.append(temp)
                    self.objectCommentCount.append(0)
        txtFile.close()

    def draw(self, screen):
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
            screen.blit(self.character[0], (self.characterPos - self.character[0].get_size()[0]/2, 300))
        if self.characterFace:
            screen.blit(pygame.transform.flip(self.character[0], 1, 0), (self.characterPos - self.character[0].get_size()[0]/2, 300))
        self.frame = (self.frame + 1) %60
        
        # objects
        if self.isHovered(self.pos) != None:
            objectNameDisplay = self.objectFont.render(self.objectNames[self.isHovered(self.pos)], 1, (255, 255, 255))
            objectNamePosition = objectNameDisplay.get_rect()
            objectNamePosition.centerx = self.pos[0]
            objectNamePosition.y = self.pos[1] + 15
            screen.blit(objectNameDisplay, objectNamePosition)

		# comments
        if self.showComment:
            commentDisplay = self.objectFont.render(self.commentText, 1, (255, 255, 255))
            commentPosition = commentDisplay.get_rect()
            commentPosition.centerx = self.characterPos
            commentPosition.y = 300 - 30
            screen.blit(commentDisplay, commentPosition)
            pygame.display.flip()
            pygame.time.delay(2500)
            self.showComment = False

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
            if self.trigger != None:
                triggerEvent = pygame.event.Event(pygame.USEREVENT, self.trigger)
                pygame.event.post(triggerEvent)
                # print self.trigger
                self.trigger = None


    def isHovered(self, pos):
        self.pos = pos
        for index, obj in enumerate(self.objectRects):
            self.isObjectHovered[index] = obj.collidepoint(pos)
        for index, obj in enumerate(self.isObjectHovered):
            if obj:
                return index
        return None

    def getClickedObject(self):
        for index, obj in enumerate(self.isObjectHovered):
            if obj:
                return index
        return None

    def onClick(self, pos):
        self.setCharacterDest(pos)

        if self.getClickedObject != None:
            self.trigger = {'trigger': self.getClickedObject()}

    def displayComment(self, trigger):
        self.showComment = True
        self.commentText = self.objectComments[trigger][self.objectCommentCount[trigger]]
        if len(self.objectComments[trigger]) < self.objectCommentCount[trigger]:
            self.objectCommentCount[trigger] += 1
