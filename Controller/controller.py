#main game loop
#controller
import pygame
import sys
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Libs')
import shapeClass



def update_model_listeners(model):
	for i in range(0,len(model.changeListeners)):
		model.changeListeners[i].refresh()
		draw_pieces(model)
		update_falling_pieces(model)
		model.changeListeners[i].draw_grid()
		model.changeListeners[i].flip()

def update_falling_pieces(model):
	for i in range(0,len(model.pieces)):
		currPiece = model.pieces[i]
		if currPiece.arrOfCoordArrs[3][0] == 7:
			currPiece.falling = False
		if currPiece.falling == True:
			#updateCoords
			print'got here'
			currPiece.move_down()


def add_change_listener(model,listener):
	model.changeListeners.append(listener)


def reset_game(model):
	for i in range(0,model.rows):
		for j in range(0,model.cols):
			model.board[i][j] = 0
	model.pieces = []


def draw_pieces(model):
	for i in range(0,len(model.pieces)):
		model.pieces[i].draw()


def add_square(model,start_col):
	sq = shapeClass.Square(model,start_col)
	model.pieces.append(sq)



#def start_button():


	

