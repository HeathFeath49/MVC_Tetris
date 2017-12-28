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
#
# GET RID OF START BUTTON FROM VIEW CLASS (USER INTERFACE)
#	-> Functionality already gotten rid of
#
# IMPLEMENT DISOLVING OF FULL ROWS
#	-> Was able to implement detection of full rows but have issues when attempting to disolve those rows
#		-> Above pieces seem to respond to a row being disolved (will fall to bottom of board after that row 
#			has been disolved) but the color of the cells that was disolved, do not change. 
#
# IMPLEMENT GAME ENDING WHEN BLOCKS REACH TOP OF BOARD
#
# IMPLEMENT POINTS SYSTEM
#	-> Give model class a point attribute and add to it as rows are dissolved
#	-> 10 points per row dissolved
#		-> Bonus points for 5 consecutive rows being dissolved   
#
# IMPLEMENT POINTS INTERFACE
#	-> Add small box in which current point value (retrieve from model's point attribute) will be displayed
#
#KNOWN BUGS:
#
# ROTATION ISSUE ON LEFT WALL 
# 	-> When rotating pieces while up against left wall, cells of shape will 
# 	appear all the way on the right side
#
# ROTATION ISSUE ON RIGHT WALL
#	-> When rotating pieces while up against the right wall, cell coords are being transformed
#   to out of range coords
#
#		POSSIBLE FIX: 
#			-> check new coords after transformation to see if they fall
#			within range of board coords. If they do not, cancel the rotation
#			 

pygame.init()

clock = pygame.time.Clock()
myModel = modelClass.Model(15,10,["O","I","J","L","S","Z","T"])
myView = viewClass.View(myModel,510,510)
myModel.add_change_listener(myView)

done = False;
while not done:
	if myModel.active_block == 0:
		check_for_full_rows(myModel)
		add_block(myModel,5)
	for event in pygame.event.get():
		#print(pygame.event.event_name(event.type))
		if event.type == pygame.QUIT:
			done = True		
		else:
			handle_input(myModel,myView,event)


	update_game(myModel)
	time.sleep(myModel.sleep_time)
	clock.tick(60)

pygame.quit()


