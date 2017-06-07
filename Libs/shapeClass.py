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

	
	def draw(self):
		raise NotImplementedError("Method not implemented")


	def getCoordinates(self):
		arr = Shape.arrOfCoordArrs
		for i in range(0,len(arr)):
			print arr[i][0]
			print arr[i][1]


class Square(Shape):

	def __init__(self,model,firstCol):
		Shape.__init__(self,model)
		self.firstCol = firstCol
		Shape.arrOfCoordArrs = [[0,firstCol],[0,firstCol+1],[1,firstCol],[1,firstCol+1]]		

	def draw(self):
		for i in range(0,len(self.arrOfCoordArrs)):
			row = self.arrOfCoordArrs[i][0]
			col = self.arrOfCoordArrs[i][1]
			self.model.board[row][col] = 1

	def move_down(self):
		for i in range(0,len(self.arrOfCoordArrs)):
			self.arrOfCoordArrs[i][0] += 1
			#refresh view

			#print self.arrOfCoordArrs		