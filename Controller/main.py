#main game loop 

import pygame
import time
import sys
from controller import *
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Libs')
import pieceClass
import shapeClass
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\View')
import viewClass
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Model')
import modelClass


pygame.init()

clock = pygame.time.Clock()
myModel = modelClass.Model(8,8)
myView = viewClass.View(myModel,510,510)
myModel.addChangeListener(myView)

done = False;
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			positionClicked = pygame.mouse.get_pos()
			
			if myView.startButton.isClicked():
				add_square(myModel,2)

			elif myView.resetButton.isClicked():
				reset_game(myModel)

	update_model_listeners(myModel)
	time.sleep(1)
	clock.tick(60)

pygame.quit()








# else: #click was within grid
# 	#set value of clicked grid location to 1
# 	row_pos = positionClicked[1]//(myView.CELL_WIDTH + myView.CELL_MARGIN)
# 	col_pos = positionClicked[0]//(myView.CELL_WIDTH + myView.CELL_MARGIN)
# 	myModel.board[row_pos][col_pos] = 1

# 	print row_pos
# 	print col_pos