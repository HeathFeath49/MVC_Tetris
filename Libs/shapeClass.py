#shapeClass
class Shape:
	arrOfCoordArrs = []
	def __init__(self,name):
		self.name = name

	#def moveDown(self):
	
	#def draw(self):
		#go through coords and set color

	def getCoordinates(self):
		arr = Shape.arrOfCoordArrs
		for i in range(0,len(arr)):
			print arr[i][0]
			print arr[i][1]


class Square(Shape):

	def __init__(self,name,firstRow,firstCol):
		Shape.__init__(self,name)
		self.firstRow = firstRow
		self.firstCol = firstCol
		Shape.arrOfCoordArrs = [[firstRow,firstCol],[firstRow,firstCol+1],[firstRow+1,firstCol],[firstRow+1,firstCol+1]]		

