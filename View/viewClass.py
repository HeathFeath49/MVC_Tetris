import pygame
import sys
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Libs')
import buttonClass
import shapeClass



class View:
	START_BTN_X = 400
	START_BTN_Y = 440
	RESET_BTN_X = 300
	RESET_BTN_Y = 440
	CELL_HEIGHT = 50
	CELL_WIDTH = 50
	CELL_MARGIN = 2
	#colors
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	GREEN = (0, 255, 0)
	RED = (255, 0, 0)
	current_draw_color = BLACK
	# list_of_colors = [BLACK,RED,GREEN,WHITE]
	pygame.font.init()
	def __init__(self,model,disX,disY):
		self.model = model
		self.screen = pygame.display.set_mode((disX,disY))
		self.screen.fill(self.WHITE)
		
		
	def determine_draw_color(self,r,c):
		cell_val = self.model.board[r][c]
		color = self.BLACK
		if cell_val == 1:
			color = self.RED
		self.current_draw_color = color
	
	def draw_grid(self):
		for r in range(0,self.model.rows):
			for c in range(0,self.model.cols):
				
				self.determine_draw_color(r,c)
				pygame.draw.rect(self.screen,
                             	self.current_draw_color,
                             	[(View.CELL_MARGIN + View.CELL_WIDTH) * c + View.CELL_MARGIN,
                              	(View.CELL_MARGIN + View.CELL_HEIGHT) * r + View.CELL_MARGIN,
                              	View.CELL_WIDTH,
                              	View.CELL_HEIGHT])

		self.resetButton = buttonClass.Button(self.screen,self.RESET_BTN_X,self.RESET_BTN_Y,75,50,self.RED,"RESET",9,self.BLACK)
		self.startButton = buttonClass.Button(self.screen,self.START_BTN_X,self.START_BTN_Y,75,50,self.GREEN,"START",9,self.BLACK)

	def flip(self):
		pygame.display.flip()

	# def createSquare(self,name,firstRow,firstCol):
	# 	return shapeClass.Square(self,name,firstRow,firstCol)
# pygame.display.flip()




