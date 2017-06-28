


class Model:

	board = []
	pieces = []
	changeListeners = []


	def __init__(self,rows,cols):
		self.rows = rows
		self.cols = cols
		for i in range(0,self.rows):
			Model.board.append([])
			for j in range(0,self.cols):
				Model.board[i].append([0])

	def add_change_listener(self,listener):
		self.changeListeners.append(listener)


	def update_change_listeners(self):
		for i in range(0,len(self.changeListeners)):
			self.changeListeners[i].refresh()
		
			self.set_all_board_values()
			self.changeListeners[i].draw_grid()
			self.changeListeners[i].flip()


	def set_all_board_values(self):
		for i in range(0,len(self.pieces)):
			self.pieces[i].set_board_values()

	def clear_model(self):
		for i in range(0,self.rows):
			for j in range(0,self.cols):
				self.board[i][j] = 0
		self.pieces = []

