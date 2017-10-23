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
	LIGHT_GREEN = (4,249,111)
	RED = (255, 0, 0)
	ORANGE = (249,131,4)
	YELLOW = (247,255,40)
	PINK = (249,4,135)
	PURPLE = (196,4,249)
	BLUE = (40,55,255)

	current_draw_color = BLACK

	pygame.font.init()

	def __init__(self,model,disX,disY):
		self.model = model
		self.screen = pygame.display.set_mode((disX,disY))
		self.screen.fill(self.WHITE)

	
	

	def determine_draw_color(self,r,c):
		cell_val = self.model.board[r][c]
		color = self.BLACK
		if cell_val != 0:  #cell is not empty
			color_number = cell_val[0]
			if color_number == 1:
				color = self.RED
			elif color_number == 2:
				color = self.PURPLE
			elif color_number == 3:
				color = self.LIGHT_GREEN
			elif color_number == 4:
				color = self.GREEN
			elif color_number == 5:
				color = self.ORANGE
			elif color_number == 6:
				color = self.PINK
			elif color_number == 7:
				color = self.BLUE
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

	def refresh(self):
		for i in range(0,self.model.rows):
			for j in range(0,self.model.cols):
				self.model.board[i][j] = 0 
		
	def flip(self):
		pygame.display.flip()





