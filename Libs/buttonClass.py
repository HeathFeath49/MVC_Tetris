#button class
import pygame
class Button: 
	def __init__(self,surface,btnX,btnY,height,width,color):
		self.surface = surface
		self.btnX = btnX
		self.btnY = btnY
		self.height = height
		self.width = width
		self.color = color
		self.button = pygame.draw.rect(self.surface,color,[self.btnX,self.btnY,self.height,self.width])

	def isClicked(self):
		clickPos = pygame.mouse.get_pos()
		return self.button.collidepoint(clickPos[0],clickPos[1])

