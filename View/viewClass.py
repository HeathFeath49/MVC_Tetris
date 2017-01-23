import pygame
white = (255,255,255)
black = (0,0,0)
class View:
	HEIGHT = 50
	WIDTH = 50
	MARGIN = 2
	def __init__(self,model,disX,disY):
		self.model = model
		self.screen = pygame.display.set_mode((disX,disY))
		self.screen.fill(white)

		for r in range(0,self.model.rows):
			for c in range(0,self.model.cols):
				pygame.draw.rect(self.screen,
                             	black,
                             	[(View.MARGIN + View.WIDTH) * c + View.MARGIN,
                              	(View.MARGIN + View.HEIGHT) * r + View.MARGIN,
                              	View.WIDTH,
                              	View.HEIGHT])
