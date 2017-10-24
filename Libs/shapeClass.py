#shapeClass
import uuid
import pygame
import sys
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Model')
import modelClass

class Block:
	arrOfCoordArrs = []
	def __init__(self,model):
		
		self.id = uuid.uuid4()
		self.model = model
		self.falling = True
		self.arrOfCoordArrs = [] 
		

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

		arr = self.arrOfCoordArrs
		for i in range(0,len(arr)):
			print arr[i][0]
			print arr[i][1]

	def set_board_values(self):

		for i in range(0,len(self.arrOfCoordArrs)):
			row = self.arrOfCoordArrs[i][0]
			col = self.arrOfCoordArrs[i][1]

			if not(row < 0):
				self.model.board[row][col] = [self.id,self.val]

	def check_for_collision(self):

		#TO DO:
			# GET RID OF REPEATING CODE

		# Bottom Collision
		for i in range(0,len(self.arrOfCoordArrs)):

			curr_coord_row = self.arrOfCoordArrs[i][0]
			curr_coord_col = self.arrOfCoordArrs[i][1]

			if curr_coord_row == self.model.rows-1:
				self.falling = False

				if self == self.model.active_block:
					self.model.remove_active_block()
				break
						
				



class O_block(Block):

	def __init__(self,model,firstCol):
		Block.__init__(self,model)
		self.firstCol = firstCol
		self.val = 1
		self.arrOfCoordArrs = [[-2,firstCol],[-2,firstCol+1],[-1,firstCol],[-1,firstCol+1]]		

class I_block(Block):

	def __init__(self,model,firstCol):
		Block.__init__(self,model)
		self.firstCol = firstCol
		self.val = 2
		self.arrOfCoordArrs = [[-4,firstCol],[-3,firstCol],[-2,firstCol],[-1,firstCol]]

class J_block(Block):

	def __init__(self,model,firstCol):
		Block.__init__(self,model)
		self.firstCol = firstCol
		self.val = 3
		self.arrOfCoordArrs = [[-3,firstCol+1],[-2,firstCol+1],[-1,firstCol+1],[-1,firstCol]]

class L_block(Block):

	def __init__(self,model,firstCol):
		Block.__init__(self,model)
		self.firstCol = firstCol
		self.val = 4
		self.arrOfCoordArrs = [[-3,firstCol],[-2,firstCol],[-1,firstCol],[-1,firstCol+1]]

class S_block(Block):

	def __init__(self,model,firstCol):
		Block.__init__(self,model)
		self.firstCol = firstCol
		self.val = 5
		self.arrOfCoordArrs = [[-1,firstCol],[-1,firstCol+1],[-2,firstCol+1],[-2,firstCol+2]]	


class Z_block(Block):

	def __init__(self,model,firstCol):
		Block.__init__(self,model)
		self.firstCol = firstCol
		self.val = 6
		self.arrOfCoordArrs = [[-2,firstCol],[-2,firstCol+1],[-1,firstCol+1],[-1,firstCol+2]]

class T_block(Block):

	def __init__(self,model,firstCol):
		Block.__init__(self,model)
		self.firstCol = firstCol
		self.val = 7
		self.arrOfCoordArrs = [[-1,firstCol-1],[-1,firstCol],[-2,firstCol],[-1,firstCol+1]]
