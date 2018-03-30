class suduku:
	def __init__(self):
		self.data = None

	def get_input_data(self):
		print "Enter data:"
		input_data = []
		for i in range(1,10):
			input_data.append(raw_input())
		matrix = []
		for row in input_data:
			row_elments = []
			for elem in row:
				if elem == "\"":
					continue
				if elem == ".":
					elem = -1
				row_elments.append(int(elem))
			matrix.append(row_elments)
		for row in matrix:
			print row



obj = suduku()
obj.get_input_data()