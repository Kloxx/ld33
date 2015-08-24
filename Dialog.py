import pygame

class Dialog:
	def __init__(self, size, txtFile):
		self.size = size
		self.char1 = []
		self.char2 = []
		self.words = []
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
                        if line == "[question]":
                                var = 3
                                continue
                        if line == "[words]":
                                var = 4
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
                txtFile.close()
		self.dialogBg = pygame.image.load("Portraits/bg_dialog.png")

        def loadText(self):
                self.txtFont = pygame.font.Font(None, self.size[1] / 20)

                # words
                self.wordBoxes = []
                self.wordSurfaces = []
                box = boxWidth, boxHeight = int(self.size[0] * 0.225), int(self.size[1] * 0.05)
                print(box)
                for i in range(12):
                        self.wordBoxes.append(pygame.Rect(
                                (self.size[0] * 0.245 * (i%4) + self.size[0] / 50,
                                 self.size[1] * 0.075 * (i/4) + self.size[1] * 0.7), box))
                for word in self.words:
                        self.wordSurfaces.append(self.txtFont.render(word, 1, self.txtColor))
                        
                               
	def draw(self, screen):
                screen.blit(self.background, (0,0))
		screen.blit(self.dialogBg, (0, self.size[1]*3/5))
		screen.blit(self.char1[0], (self.size[0]*1/6 - self.char1[0].get_size()[0]/2, self.size[1]*0.4))
		screen.blit(self.char2[0], (self.size[0]*5/6 - self.char2[0].get_size()[0]/2, self.size[1]*0.4))
                for index, box in enumerate(self.wordBoxes):
                        if index < len(self.words):
                                pygame.draw.rect(screen, (255,255,255), box)
                                screen.blit(self.wordSurfaces[index],
                                            (box.centerx - self.wordSurfaces[index].get_width() / 2,
                                             box.centery - self.wordSurfaces[index].get_height() / 2))
                        else:
                                pygame.draw.rect(screen, (120,120,120), box)

	def draw_menu(self, screen):
		menu_font = pygame.font.Font(None, 36)
		questionDisplay = menu_font.render(question, 1, (255, 255, 255))
		questionPosition = questionDisplay.get_rect()
		questionPosition.centerx = screen.get_rect().centerx
		questionPosition.y = self.size[1]*0.7
		screen.blit(questionDisplay, questionPosition)
		
		nbWords = len(words)

		options = []
		
		for index, word in enumerate(words):
			option = Option(word, ((self.size[0]/(nbWords+1))*(1+index), self.size[1]*0.8), menu_font, screen)
			options.append(option)
			
		for option in options:
			if option.rect.collidepoint(pygame.mouse.get_pos()):
				option.hovered = True
			else:
				option.hovered = False
			option.draw()

class Option:

	hovered = False

	def __init__(self, text, pos, menu_font, screen):
		self.text = text
		self.pos = pos
		self.menu_font = menu_font
		self.screen = screen
		self.set_rect()
		self.draw()

	def draw(self):
		self.set_rend()
		self.screen.blit(self.rend, self.rect)

	def set_rend(self):
		self.rend = self.menu_font.render(self.text, True, self.get_color())

	def get_color(self):
		if self.hovered:
			return (255, 255, 255)
		else:
			return (100, 100, 100)
		
	def set_rect(self):
		self.set_rend()
		self.rect = self.rend.get_rect()
		self.rect.topleft = self.pos

class Dictionary:

	def __init__(self):
		self.words = []
		dict = open("Dialogs/dictionary.txt", 'r')

		for index, line in enumerate(dialogFile.read().split("\n")):
			words.append(line)
