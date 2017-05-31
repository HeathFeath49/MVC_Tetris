class Model:

	board = []
	changeListeners = []
	def __init__(self,rows,cols):
		self.rows = rows
		self.cols = cols
		for i in range(0,self.rows):
			Model.board.append([])
			for j in range(0,self.cols):
				Model.board[i].append([0])

	#def addSquareToBoard(self,firstRow,firstcol):


	def addChangeListener(self,listener):
		Model.changeListeners.append(listener)

	# def notifyChangeListeners(self,change):
	# 	for i in range(0,len(Model.changeListeners)):
	# 		currView = Model.changeListeners[i]
	# 		currView.change()
