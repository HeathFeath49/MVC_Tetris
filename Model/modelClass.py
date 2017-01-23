class Model:

	board = []

	def __init__(self,rows,cols):
		self.rows = rows
		self.cols = cols
		for i in range(0,self.rows):
			Model.board.append([])
			for j in range(0,self.cols):
				Model.board[i].append([""])


