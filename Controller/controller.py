#controller
import pygame 
import sys
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Libs')
import shapeClass
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\View')
import viewClass



def update_game(model):

	update_piece_position(model)
	model.update_change_listeners()


def reset_game(model):

	model.clear_model()


def handle_input(model,view,event):
	if model.active_block:
		model.active_block.check_for_collision()
	#handle mouse clicks
	if event.type == pygame.MOUSEBUTTONDOWN:
		positionClicked = pygame.mouse.get_pos()
		if view.startButton.isClicked():
			add_block(model,5)

		elif view.resetButton.isClicked():
			reset_game(model)

	#handle key presses
	if event.type == pygame.KEYDOWN:
		if model.active_block: #check if there is an active block
			if event.key == 276: #left
				if model.active_block.can_move_left:
					model.active_block.move_left()
			elif event.key == 275: #right
				if model.active_block.can_move_right:
		 			model.active_block.move_right()



def update_piece_position(model):
	for i in range(0,len(model.pieces)):

		currPiece = model.pieces[i]
		currPiece.check_for_collision()

		if currPiece.falling == True:
			currPiece.move_down()
			

def add_block(model,start_col):

	new_block = shapeClass.S_block(model,start_col)
	model.pieces.append(new_block)
	model.set_active_block(new_block)



	

