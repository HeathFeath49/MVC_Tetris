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
		self.can_move_left = True
		self.can_move_right = True
		self.can_move_down = True
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
			#GET RID OF REPEATING CODE!!
			#Consider breaking collison function into seperate functions
			#Consider replacing for loop with while loop
			#Add horizontal detetion of other blocks
	
		# Bottom Collision
		for i in range(0,len(self.arrOfCoordArrs)):

			curr_coord_row = self.arrOfCoordArrs[i][0]
			curr_coord_col = self.arrOfCoordArrs[i][1]
			#print(curr_coord_col)
			if not(curr_coord_row < 0):
				#check if last row
				if curr_coord_row == self.model.rows-1:
					self.can_move_down = False

					if self == self.model.active_block:
						self.model.remove_active_block()
					break
				#check if another block in the way
				elif((self.model.board[curr_coord_row+1][curr_coord_col]) != [0]):
					
					if self.model.board[curr_coord_row+1][curr_coord_col][0] != self.id:
						self.can_move_down = False
						if self == self.model.active_block:
							self.model.remove_active_block()
						break


		# Left/Right collision 				
		for i in range(0,len(self.arrOfCoordArrs)):
			curr_coord_row = self.arrOfCoordArrs[i][0]
			curr_coord_col = self.arrOfCoordArrs[i][1]
			
			#check right wall collision

			if(curr_coord_col == self.model.cols-1):
				self.can_move_right = False
				break
			else:
				self.can_move_right = True		

			#check for block to right

			if (self.model.board[curr_coord_row][curr_coord_col+1] != [0]):
				if(self.model.board[curr_coord_row][curr_coord_col+1][0] != self.id):
					self.can_move_right = False
					break
			else:
				self.can_move_right = True


			#check left wall collision

			if (curr_coord_col == 0):
				self.can_move_left = False
				break
			else:
				self.can_move_left = True


			#check for block to left

			if (self.model.board[curr_coord_row][curr_coord_col-1] != [0]):
				if(self.model.board[curr_coord_row][curr_coord_col-1][0] != self.id):
					self.can_move_left = False
					break
			else:
				self.can_move_left = True

	def check_for_collision_V2(self):
		# BOOLS keeping track of
		bottom_collision_detected = False
		left_collision_detected = False
		right_collision_detected = False

		# Bottom Collision
		i = 0
		while(i < len(self.arrOfCoordArrs) and bottom_collision_detected == False):
			curr_coord_row = self.arrOfCoordArrs[i][0]
			curr_coord_col = self.arrOfCoordArrs[i][1]

			if not(curr_coord_row < 0):
				#check if last row
				if (curr_coord_row == self.model.rows-1):
					bottom_collision_detected = True

				#check for block in the way
				elif((self.model.board[curr_coord_row+1][curr_coord_col]) != [0]):
					if (self.model.board[curr_coord_row+1][curr_coord_col][0] != self.id):
						bottom_collision_detected = True

			i+=1

		# Left Collision Detection
		i = 0
		while(i< len(self.arrOfCoordArrs) and left_collision_detected == False):
			curr_coord_row = self.arrOfCoordArrs[i][0]
			curr_coord_col = self.arrOfCoordArrs[i][1]

			#check left wall
			if (curr_coord_col == 0):
				left_collision_detected = True
			#check for block to left
			elif(self.model.board[curr_coord_row][curr_coord_col-1] != [0]):
				if(self.model.board[curr_coord_row][curr_coord_col-1][0] != self.id):
					left_collision_detected = True

			i+=1		

		#Right Collision Detection
		i = 0
		while(i< len(self.arrOfCoordArrs) and right_collision_detected == False):
			curr_coord_row = self.arrOfCoordArrs[i][0]
			curr_coord_col = self.arrOfCoordArrs[i][1]

			#check right wall
			if (curr_coord_col == self.model.cols-1):
				right_collision_detected = True
			#check for block to right
			elif(self.model.board[curr_coord_row][curr_coord_col+1] != [0]):
				if(self.model.board[curr_coord_row][curr_coord_col+1][0] != self.id):
					right_collision_detected = True
			i+=1

		#check bools
		if(left_collision_detected):
			print('left collision detected')
			self.can_move_left = False
		else:
			self.can_move_left = True

		if(right_collision_detected):
			print('right collision detected')
			self.can_move_right = False
		else:
			self.can_move_right = True

		if(bottom_collision_detected):
			print('bottom collision')
			self.can_move_down = False
			if(self == self.model.active_block):
				self.model.remove_active_block()
		else:
			self.can_move_down = True	


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
