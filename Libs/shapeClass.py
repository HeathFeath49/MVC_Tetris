#shapeClass
import pygame
import sys
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Model')
import modelClass

class Shape:
	arrOfCoordArrs = []
	def __init__(self,model):
		#self.name = name
		self.model = model
		self.falling = True
		self.arrOfCoordArrs = [] 

	
	def draw(self):
		raise NotImplementedError("Method not implemented")

	def move_down(self):
		for i in range(0,len(self.arrOfCoordArrs)):
			self.arrOfCoordArrs[i][0] += 1

	def move_left(self):
		for i in range(0,len(self.arrOfCoordArrs)):
			self.arrOfCoordArrs[i][1] -= 1

	def move_right(self):
		for i in range(0,len(self.arrOfCoordArrs)):
			self.arrOfCoordArrs[i][1] += 1


	def getCoordinates(self):
		arr = Shape.arrOfCoordArrs
		for i in range(0,len(arr)):
			print arr[i][0]
			print arr[i][1]


class Square(Shape):

	def __init__(self,model,firstCol):
		Shape.__init__(self,model)
		self.firstCol = firstCol
		self.arrOfCoordArrs = [[0,firstCol],[0,firstCol+1],[1,firstCol],[1,firstCol+1]]
		self.val = 1		

	def set_board_values(self):
		for i in range(0,len(self.arrOfCoordArrs)):
			row = self.arrOfCoordArrs[i][0]
			col = self.arrOfCoordArrs[i][1]
			self.model.board[row][col] = self.val

	
