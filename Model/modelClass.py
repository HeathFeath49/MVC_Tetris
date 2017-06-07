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

	def addChangeListener(self,listener):
	 	Model.changeListeners.append(listener)
