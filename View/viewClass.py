import pygame
import sys
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Libs')
import buttonClass
import shapeClass
pygame.font.init()


class View:
	START_BTN_X = 100
	START_BTN_Y = 440
	RESET_BTN_X = 200
	RESET_BTN_Y = 440
	CELL_HEIGHT = 25
	CELL_WIDTH = 25
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

	#fonts
	SCORE_FONT = pygame.font.SysFont('Comic Sans MS', 30)

	#other attributes
	current_draw_color = BLACK

	

	def __init__(self,model,disX,disY):
		self.model = model
		self.screen = pygame.display.set_mode((disX,disY))
		self.screen.fill(self.WHITE)

	
	

	def determine_draw_color(self,r,c):
		cell_val = self.model.board[r][c]
		color = self.BLACK
	
		if cell_val != [0]:  #cell is not empty
			color_number = cell_val[1]
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

	def display_score(self):
		textsurface = self.SCORE_FONT.render('Score: '+ str(self.model.score), True, (0, 0, 0))
		self.screen.blit(textsurface,(350,0))
	
	def draw_grid(self):
		self.screen.fill(self.WHITE)
		for r in range(0,self.model.rows):
			for c in range(0,self.model.cols):
				
				self.determine_draw_color(r,c)
				pygame.draw.rect(self.screen,
                             	self.current_draw_color,
                             	[(View.CELL_MARGIN + View.CELL_WIDTH) * c + View.CELL_MARGIN+32,
                              	(View.CELL_MARGIN + View.CELL_HEIGHT) * r + View.CELL_MARGIN,
                              	View.CELL_WIDTH,
                              	View.CELL_HEIGHT])

		self.resetButton = buttonClass.Button(self.screen,self.RESET_BTN_X,self.RESET_BTN_Y,75,40,self.RED,"RESET",9,self.BLACK)	
		self.display_score()

	def refresh(self):
		for i in range(0,self.model.rows):
			for j in range(0,self.model.cols):
				self.model.board[i][j] = [0]

				
		
	def flip(self):
		pygame.display.flip()





