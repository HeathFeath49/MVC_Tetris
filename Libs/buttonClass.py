#button class
import pygame
from textHelperMethods import applyTextToButton
class Button: 
	def __init__(self,surface,btnX,btnY,height,width,color,text,font_size,font_color):
		self.surface = surface
		self.btnX = btnX
		self.btnY = btnY
		self.height = height
		self.width = width
		self.color = color
		self.button = pygame.draw.rect(self.surface,color,[self.btnX,self.btnY,self.height,self.width])
		applyTextToButton(self,text,font_size,font_color)

	def isClicked(self):
		clickPos = pygame.mouse.get_pos()
		return self.button.collidepoint(clickPos[0],clickPos[1])



