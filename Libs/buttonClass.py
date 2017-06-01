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


	






	# def text_objects(self,text, font):
	# 	textSurface = font.render(text, True, (0,0,0))
	# 	return textSurface, textSurface.get_rect()	

	# def applyText(self,text):
	# 	smallText = pygame.font.Font("freesansbold.ttf",9)
	# 	textSurf, textRect = self.text_objects(text, smallText)
	# 	textRect.center = ((self.btnX+(self.height/2)),(self.btnY+(self.width/2)))
	# 	self.surface.blit(textSurf,textRect)


