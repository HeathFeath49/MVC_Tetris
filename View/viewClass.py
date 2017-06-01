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
	current_draw_color = BLACK
	list_of_colors = [BLACK,RED,GREEN,WHITE]
	pygame.font.init()
	def __init__(self,model,disX,disY):
		self.model = model
		self.screen = pygame.display.set_mode((disX,disY))
		self.screen.fill(WHITE)
		
	def determine_draw_color(self,r,c):
		cell_val = self.model.board[r][c]
		color = BLACK
		if cell_val == 1:
			color = RED
		self.current_draw_color = color
	
	def draw_grid(self):
		for r in range(0,self.model.rows):
			for c in range(0,self.model.cols):
				
				self.determine_draw_color(r,c)
				pygame.draw.rect(self.screen,
                             	self.current_draw_color,
                             	[(View.MARGIN + View.WIDTH) * c + View.MARGIN,
                              	(View.MARGIN + View.HEIGHT) * r + View.MARGIN,
                              	View.WIDTH,
                              	View.HEIGHT])

		self.testButton = buttonClass.Button(self.screen,View.BTNX,View.BTNY,75,50,RED,"ADD SQUARE",9,BLACK)

	def flip(self):
		pygame.display.flip()

	# def createSquare(self,name,firstRow,firstCol):
	# 	return shapeClass.Square(self,name,firstRow,firstCol)
# pygame.display.flip()




