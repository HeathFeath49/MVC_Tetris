#controller
import pygame 
import sys
from random import randint
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Libs')
import shapeClass
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\View')
import viewClass

#TO DO:
# rename update_piece_position function
# get rid of start button 
# implement continous falling pieces

def update_game(model):

	update_piece_position(model)
	model.update_change_listeners()


def reset_game(model):

	model.clear_model()


def handle_input(model,view,event):

	#handle mouse clicks
	if event.type == pygame.MOUSEBUTTONDOWN:
		positionClicked = pygame.mouse.get_pos()
		if view.resetButton.isClicked():
			reset_game(model)

	#handle key presses
	if event.type == pygame.KEYDOWN:
		if model.active_block: #check if there is an active block
			if event.key == 276: #left arrow
				model.active_block.check_left_collision()
				if model.active_block.can_move_left:
					model.active_block.move_left()
			elif event.key == 275: #right arrow
				model.active_block.check_right_collision()
				if model.active_block.can_move_right:
		 			model.active_block.move_right()

		 	if event.key == 114: # R
		 		model.active_block.rotate_block()



def update_piece_position(model):
	for i in range(0,len(model.blocks_on_board)):

		currPiece = model.blocks_on_board[i]
		currPiece.check_bottom_collision()

		if currPiece.can_move_down == True:
			currPiece.move_down()

			
			

def add_block(model,start_col):
	rand_num = randint(0,6)
	block_letter = model.arr_of_block_types[rand_num]

	if(block_letter == "O"):
		new_block = shapeClass.O_block(model,start_col)
	elif(block_letter == "I"):
		new_block = shapeClass.I_block(model,start_col)
	elif(block_letter == "J"):
		new_block = shapeClass.J_block(model,start_col)
	elif(block_letter == "L"):
		new_block = shapeClass.L_block(model,start_col)
	elif(block_letter == "S"):
		new_block = shapeClass.S_block(model,start_col)
	elif(block_letter == "Z"):
		new_block = shapeClass.Z_block(model,start_col)
	elif(block_letter == "T"):			
		new_block = shapeClass.T_block(model,start_col)

	model.blocks_on_board.append(new_block)
	model.set_active_block(new_block)



	

