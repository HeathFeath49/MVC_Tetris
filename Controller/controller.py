#main game loop
#controller
import pygame
import sys
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Libs')
import pieceClass
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\View')
import viewClass
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Model')
import modelClass

myModel = modelClass.Model(8,8)
myView = viewClass.View(myModel,510,510)


def buttonClicked(btnPosx,btnPosy):
	clickPos = pygame.mouse.get_pos()
	return myView.button.collidepoint(clickPos[0],clickPos[1])

pygame.init()


done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			positionClicked = pygame.mouse.get_pos()
			#check if button clicked
			if buttonClicked(myView.BTNX,myView.BTNY):
			 	print "button has been clicked"
			

	myView.flip()

pygame.quit()