import pygame
import sys
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Libs')
import buttonClass
import shapeClass

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class View:
	BTNX = 400
	BTNY = 440
	HEIGHT = 50
	WIDTH = 50
	MARGIN = 2
	pygame.font.init()
	def __init__(self,model,disX,disY):
		self.model = model
		self.screen = pygame.display.set_mode((disX,disY))
		self.screen.fill(WHITE)
		#self.font = pygame.font.get_default_font()
		#self.font_renderer = pygame.font.Font(default_font,size)
		# self.button = pygame.draw.rect(self.screen,RED,[View.BTNX,View.BTNY,75,50])
		self.testButton = buttonClass.Button(self.screen,View.BTNX,View.BTNY,75,50,RED)
		#draw board
		for r in range(0,self.model.rows):
			for c in range(0,self.model.cols):
				pygame.draw.rect(self.screen,
                             	BLACK,
                             	[(View.MARGIN + View.WIDTH) * c + View.MARGIN,
                              	(View.MARGIN + View.HEIGHT) * r + View.MARGIN,
                              	View.WIDTH,
                              	View.HEIGHT])
		#draw button
	def flip(self):
		pygame.display.flip()

	#def createSquare(self):

# pygame.display.flip()




