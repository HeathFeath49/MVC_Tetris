class Model:

	board = []
	blocks_on_board = []
	num_of_blocks = 0
	score = 0
	changeListeners = []
	sleep_time = .5
	active_block = 0


	def __init__(self,rows,cols,arr_of_block_types):
		self.rows = rows
		self.cols = cols
		self.arr_of_block_types = arr_of_block_types
		for i in range(0,self.rows):
			Model.board.append([])
			for j in range(0,self.cols):
				Model.board[i].append([0])

	def add_change_listener(self,listener):
		self.changeListeners.append(listener)

	#TO DO: Move all view method calls to the refresh method 
	def update_change_listeners(self):
		for i in range(0,len(self.changeListeners)):
			self.changeListeners[i].refresh()
			self.set_all_board_values()
			self.changeListeners[i].draw_grid()
			self.changeListeners[i].flip()

	def set_all_board_values(self):
		for i in range(0,len(self.blocks_on_board)):
			self.blocks_on_board[i].set_board_values()

	def clear_model(self):
		for i in range(0,self.rows):
			for j in range(0,self.cols):
				self.board[i][j] =  0
		self.blocks_on_board = []
		self.num_of_blocks = 0
		self.active_block = 0

	def set_active_block(self,block):
		self.active_block = block

	def remove_active_block(self):
		self.active_block = 0




