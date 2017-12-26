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

#TO DO:
# CLEAN UP USER INTERFACE
# IMPLEMENT ABILITY TO SPEED UP FALL
# IMPLEMENT DISOLVING OF FULL ROWS
# IMPLEMENT POINTS SYSTEM 
# IMPLEMENT POINTS INTERFACE

pygame.init()

clock = pygame.time.Clock()
myModel = modelClass.Model(15,10,["O","I","J","L","S","Z","T"])
myView = viewClass.View(myModel,510,510)
myModel.add_change_listener(myView)

done = False;
while not done:
	if myModel.active_block == 0:
		add_block(myModel,5)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True		
		else:
			handle_input(myModel,myView,event)


	update_game(myModel)
	time.sleep(myModel.sleep_time)
	clock.tick(60)

pygame.quit()


