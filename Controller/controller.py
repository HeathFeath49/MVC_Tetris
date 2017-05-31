#main game loop
#controller
import pygame
import sys
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Libs')
import pieceClass
import shapeClass
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\View')
import viewClass
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Model')
import modelClass




# def buttonClicked(btnPosx,btnPosy):
# 	clickPos = pygame.mouse.get_pos()
# 	return myView.button.collidepoint(clickPos[0],clickPos[1])

pygame.init()

myModel = modelClass.Model(8,8)
myView = viewClass.View(myModel,510,510)
myModel.addChangeListener(myView)
#myModel.notifyChangeListeners("sayHello")
done = False;
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			positionClicked = pygame.mouse.get_pos()
			#check if button clicked
			if myView.testButton.isClicked():
				print "button has been clicked"
				mySquare = shapeClass.Square("square1",0,0)
				print mySquare.arrOfCoordArrs
			 

	myView.flip()

pygame.quit()