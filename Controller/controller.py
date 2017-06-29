#controller
import pygame
import sys
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Libs')
import shapeClass



def update_game(model):
	update_piece_position(model)
	model.update_change_listeners()


def reset_game(model):
	model.clear_model()


def update_piece_position(model):
	for i in range(0,len(model.pieces)):
		currPiece = model.pieces[i]
		print currPiece.arrOfCoordArrs
		if currPiece.arrOfCoordArrs[len(currPiece.arrOfCoordArrs)-1][0] == model.rows-1:
			currPiece.falling = False
		if currPiece.falling == True:
			currPiece.move_down()
			

def add_block(model,start_col):
	#sq = shapeClass.Square(model,start_col)
	model.pieces.append(shapeClass.T_block(model,start_col))

	

