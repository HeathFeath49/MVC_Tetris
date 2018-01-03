#controller
import pygame 
import sys
from random import randint
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

		 	if event.key == 274: #down arrow
		 		model.sleep_time = .1

		 	if event.key == 114: # R
		 		model.active_block.rotate_block()

	if event.type == pygame.KEYUP:
		if event.key == 274: #down arrow
			model.sleep_time = .5


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
	

def check_for_full_rows(model):
	#TO DO:
	# DISOLVE FULL ROWS

	list_of_full_rows = [] #list to keep track of num of rows that are full
	keep_going = True # Want to stop if you cannot find any full rows or there are no more full rows
	i = model.rows-1

	while(i > 0 and keep_going):
		j = 0
		empty_cell_found = False

		while(j < model.cols-1 and not empty_cell_found):
			#print(i)
			#print(j)
			if(model.board[i][j] == [0]):
				empty_cell_found = True
			j+=1
		
		if not(empty_cell_found):
			list_of_full_rows.append(i)	

		i-=1

	if(len(list_of_full_rows) > 0):
		print(list_of_full_rows)
		disolve_rows(model,list_of_full_rows)


def disolve_rows(model,list_of_row_nums):
	#print('called disolve row')

	for r in range(0,len(list_of_row_nums)):
		num_of_row = list_of_row_nums[r]
		add_to_score(model,10)
		for c in range(0,model.cols-1):
			cell_data = model.board[num_of_row][c]
			
			#get index of shape in arr via shape's id
			index_of_shape = cell_data[0] 
			
			curr_shape = model.blocks_on_board[index_of_shape]

			index_of_coord_arr_to_set = cell_data[2]

			#set val
			curr_shape.arrOfCoordArrs[index_of_coord_arr_to_set] = [0]

			model.board[num_of_row][c] = [0]


def add_to_score(model,num_points):
	model.score += num_points

	

