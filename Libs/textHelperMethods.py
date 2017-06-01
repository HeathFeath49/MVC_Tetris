#textHelperMethods

import pygame

def text_objects(text,font,font_color):
		textSurface = font.render(text, True, font_color)
		return textSurface, textSurface.get_rect()

def applyTextToButton(btn,text,font_size,font_color):
		smallText = pygame.font.Font("freesansbold.ttf",font_size)
		textSurf, textRect = text_objects(text, smallText,font_color)
		textRect.center = ((btn.btnX+(btn.height/2)),(btn.btnY+(btn.width/2)))
		btn.surface.blit(textSurf,textRect)