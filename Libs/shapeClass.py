#shapeClass
import pygame
import uuid
import numpy
import sys
sys.path.insert(0, 'C:\Users\Heather\Desktop\projects\MVC_Practice\Model')
import modelClass

#TO DO:
# ADD COMMENTS TO ROTATION FUNCTION

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

	def rotate_block(self):
		for i in range(0,len(self.arrOfCoordArrs)):
			curr_coords = self.arrOfCoordArrs[i]
			pivot_cell = self.arrOfCoordArrs[1]

			#vectors/matrices
			rotation_matrix = numpy.array([[0,1],[-1,0]])
			pivot_vector = numpy.array(pivot_cell)
			curr_coord_as_vector = numpy.array(curr_coords)
			relative_vector = (curr_coord_as_vector - pivot_vector)
			transformed_relative_vector = rotation_matrix.dot(relative_vector)
			absolute_coords = pivot_vector+transformed_relative_vector
			
			new_row = absolute_coords[0]
			new_col = absolute_coords[1]

			self.arrOfCoordArrs[i][0] = new_row
			self.arrOfCoordArrs[i][1] = new_col

	def check_bottom_collision(self):
		bottom_collision_detected = False
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
		#check bools
		if(bottom_collision_detected):
			self.can_move_down = False
			if(self == self.model.active_block):
				self.model.remove_active_block()
				#NOW WOULD BE THE TIME TO CHECK FOR FULL ROWS
		else:
			self.can_move_down = True	

	def check_left_collision(self):
		left_collision_detected = False
		# Left Collision Detection
		i = 0
		while(i< len(self.arrOfCoordArrs) and left_collision_detected == False):
			curr_coord_row = self.arrOfCoordArrs[i][0]
			curr_coord_col = self.arrOfCoordArrs[i][1]
			if not(curr_coord_row < 0):
				#check left wall
				if (curr_coord_col == 0):
					left_collision_detected = True
				#check for block to left
				elif(self.model.board[curr_coord_row][curr_coord_col-1] != [0]):
					if(self.model.board[curr_coord_row][curr_coord_col-1][0] != self.id):
						left_collision_detected = True

			i+=1	
		#check bools
		if(left_collision_detected):
			self.can_move_left = False
		else:
			self.can_move_left = True

	def check_right_collision(self):
		right_collision_detected = False			
		#Right Collision Detection
		i = 0
		while(i< len(self.arrOfCoordArrs) and right_collision_detected == False):
			curr_coord_row = self.arrOfCoordArrs[i][0]
			curr_coord_col = self.arrOfCoordArrs[i][1]
			if not(curr_coord_row < 0):
				#check right wall
				if (curr_coord_col == self.model.cols-1):
					right_collision_detected = True
				#check for block to right
				elif(self.model.board[curr_coord_row][curr_coord_col+1] != [0]):
					if(self.model.board[curr_coord_row][curr_coord_col+1][0] != self.id):
						right_collision_detected = True
			i+=1

		#check bool
		if(right_collision_detected):
			self.can_move_right = False
		else:
			self.can_move_right = True


# subclass of Blocks
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
