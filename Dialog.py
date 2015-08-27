import pygame

class Dialog:
	def __init__(self, size, txtFile):
		self.size = size
		self.char1 = []
		self.char2 = []
		self.char2state = 0
		self.words = []
		self.answerCheck = {}
		self.answerCode = ""
		self.answer = []
		self.wait = False
		self.isWordUsed = []
		self.txtColor = 0, 0, 0
		self.loadAssets(txtFile)
		self.loadText()

	def loadAssets(self, txtFile):
                """
                txtFile(str) -> None
                Text parser for assets and text informations
                """
                var = None
                txtFile = open(txtFile, "r")
                for line in txtFile.read().split("\n"):
                        if line == "[character1]":
                                var = 0
                                continue
                        if line == "[character2]":
                                var = 1
                                continue
                        if line == "[background]":
                                var = 2
                                continue
                        if line == "[question]":
                                var = 3
                                continue
                        if line == "[words]":
                                var = 4
                                continue
                        if line == "[answers]":
                                var = 5
                                continue
                        if line == "[other]":
                                break
                        if line:
                                if var == 0:
                                        self.char1.append(pygame.image.load(line).convert_alpha())
                                if var == 1:
                                        self.char2.append(pygame.image.load(line).convert_alpha())
                                if var == 2:
                                        self.background = pygame.transform.scale(pygame.image.load(line).convert(), self.size)
                                if var == 3:
                                        self.questionTxt = line
                                if var == 4:
                                        self.words.append(line)
                                if var == 5:
                                        key,value = line.split(":")
                                        self.answerCheck[key] = value
                txtFile.close()
		self.dialogBg = pygame.image.load("Portraits/bg_dialog.png")

        def loadText(self):
                """
                Creates text Surfaces
                """
                self.txtFont = pygame.font.Font(None, self.size[1] / 20)

                # words
                self.wordBoxes = []
                self.wordSurfaces = []
                box = boxWidth, boxHeight = int(self.size[0] * 0.225), int(self.size[1] * 0.05)
                for i in range(12):
                        self.wordBoxes.append(pygame.Rect(
                                (self.size[0] * 0.245 * (i%4) + self.size[0] / 50,
                                 self.size[1] * 0.075 * (i/4) + self.size[1] * 0.7), box))
                        if i < len(self.words):
                                self.isWordUsed.append(False)
                        else:
                                self.isWordUsed.append(True)
                for word in self.words:
                        self.wordSurfaces.append(self.txtFont.render(word, 1, self.txtColor))

                # others
                self.question = self.txtFont.render(self.questionTxt, 1, self.txtColor)
                self.confirmBox = pygame.Rect((self.size[0] * 5/8, self.size[1] * 37/40),
                                              (self.size[0] * 0.125, boxHeight))
                self.cancelBox = pygame.Rect((self.size[0] * 13/16, self.size[1] * 37/40),
                                             (self.size[0] * 0.125, boxHeight))
                self.answerSurface = self.txtFont.render("", 1, self.txtColor)
                               
	def draw(self, screen):
                """
                screen(pygame.Surface) -> None
                Blits all elements to screen
                """
                screen.blit(self.background, (0,0))
		screen.blit(pygame.transform.flip(self.char1[0], 1, 0), (self.size[0]*1/6 - self.char1[0].get_size()[0]/2, self.size[1]*0.15))
		screen.blit(self.char2[0], (self.size[0]*5/6 - self.char2[0].get_size()[0]/2, self.size[1]*0.15))
		screen.blit(self.dialogBg, (0, self.size[1]*3/5))
		screen.blit(self.question, (self.size[0]/2 - self.question.get_width()/2, self.size[1]*5/8))
                screen.blit(self.answerSurface, (self.size[0]*5/16 - self.answerSurface.get_width()/2, self.size[1]*37/40))
                for index, box in enumerate(self.wordBoxes):
                        if index < len(self.words):
                                if self.isWordUsed[index]:
                                        pygame.draw.rect(screen, (120,120,120), box)
                                else:
                                        pygame.draw.rect(screen, (255,255,255), box)
                                screen.blit(self.wordSurfaces[index],
                                            (box.centerx - self.wordSurfaces[index].get_width() / 2,
                                             box.centery - self.wordSurfaces[index].get_height() / 2))
                        else:
                                pygame.draw.rect(screen, (120,120,120), box)
                pygame.draw.rect(screen, (0,255,0), self.confirmBox)
                pygame.draw.rect(screen, (255,0,0), self.cancelBox)
                if self.wait:
                        pygame.time.delay(500)
                

        def isBoxClicked(self, pos):
                """
                pos(int) -> None
                pos(int) -> Value of the reaction (int)
                Checks if one of the box is clicked. Calls checkAnswer() if confirm box is clicked.
                """
                for index, box in enumerate(self.wordBoxes):
                        if box.collidepoint(pos) and not self.isWordUsed[index] and len(self.answerCode) < 3:
                                self.answerCode += "%0.1X" % index
                                self.answer.append(self.words[index])
                                self.isWordUsed[index] = True
                                print(self.answerCode)
                                print(self.answer)
                if self.confirmBox.collidepoint(pos) and len(self.answerCode):
                        return self.checkAnswer(self.answerCode)
                if self.cancelBox.collidepoint(pos) and len(self.answerCode):
                        self.isWordUsed[int(self.answerCode[-1], 16)] = False
                        self.answerCode = self.answerCode[:-1]
                        self.answer = self.answer[:-1]
                        print(self.answerCode)
                        print(self.answer)
                self.answerSurface = self.txtFont.render(" ".join(self.answer), 1, self.txtColor)
                return None

        def checkAnswer(self, key):
                """
                key(str) -> None
                key(str) -> Value of the reaction (int)
                Checks if answer in key exists in *answerCheck* dict. Returns the value if yes.
                """
                if key in self.answerCheck:
                        print("reaction : ", self.answerCheck[key])
                        self.char2state = int(self.answerCheck[key]) % 2
                        self.resetAnswer()
                        if not int(self.answerCheck[key]):
                                return int(self.answerCheck[key])
                else:
                        self.resetAnswer()

        def resetAnswer(self):
                """
                Resets answer text and key.
                """
                pygame.time.delay(500)
                self.answerCode = ""
		self.answer = []
		self.answerSurface = self.txtFont.render("", 1, self.txtColor)
                for i in range(12):
                        if i < len(self.words):
                                self.isWordUsed[i] = False
                        else:
                                self.isWordUsed[i] = True

        def changeQuestion(self, text):
                """
                text(str) -> None
                Changes string in *questionTxt* to *text* and renders to Surface.
                """
                self.questionTxt = text
                self.question = self.txtFont.render(self.questionTxt, 1, self.txtColor)
                self.wait = True

class Dialog2:
	def __init__(self, size, txtFile):
		self.size = size
		self.char1 = []
		self.char2 = []
		self.char2state = 0
		self.dialog = []
		self.marker = 0
		self.txtColor = 0, 0, 0
		self.loadAssets(txtFile)
		self.loadText()

	def loadAssets(self, txtFile):
                var = None
                txtFile = open(txtFile, "r")
                for line in txtFile.read().split("\n"):
                        if line == "[character1]":
                                var = 0
                                continue
                        if line == "[character2]":
                                var = 1
                                continue
                        if line == "[background]":
                                var = 2
                                continue
                        if line == "[dialog]":
                                var = 3
                                continue
                        if line:
                                if var == 0:
                                        self.char1.append(pygame.image.load(line).convert_alpha())
                                if var == 1:
                                        self.char2.append(pygame.image.load(line).convert_alpha())
                                if var == 2:
                                        self.background = pygame.transform.scale(pygame.image.load(line).convert(), self.size)
                                if var == 3:
                                        self.dialog.append(line)
                txtFile.close()
		self.dialogBg = pygame.image.load("Portraits/bg_dialog.png")

        def loadText(self):
                self.txtFont = pygame.font.Font(None, self.size[1] / 10)
                              
	def draw(self, screen):
                screen.blit(self.background, (0,0))
		screen.blit(pygame.transform.flip(self.char1[0], 1, 0), (self.size[0]*1/6 - self.char1[0].get_size()[0]/2, self.size[1]*0.2))
		screen.blit(self.char2[self.char2state], (self.size[0]*5/6 - self.char2[0].get_size()[0]/2, self.size[1]*0.2))
		screen.blit(self.dialogBg, (0, self.size[1]*3/5))
		text = self.txtFont.render(self.dialog[self.marker], 1, self.txtColor)
		screen.blit(text, (self.size[0]/2 - text.get_width()/2, self.size[1]*5/8))

	def nextSentence(self):
                self.marker += 1
                if self.marker < len(self.dialog):
                        return False
                else:
                        return True
