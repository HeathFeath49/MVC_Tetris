#main game loop
#controller
import pygame
import sys
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Libs')
import shapeClass

def add_square(model,start_col):
	sq = shapeClass.Square(model,start_col)
	model.pieces.append(sq)


def reset_model(model):
	for i in range(0,model.rows):
		for j in range(0,model.cols):
			model.board[i][j] = 0

def draw_pieces(model):
	for i in range(0,len(model.pieces)):
		model.pieces[i].draw()

#def start_button():


	

