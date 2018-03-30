class calculate_power:
	def __init__(self):
		pass
	def get_power_value(self, x, n):
		if n == 0:
			return 1
		pow_value = self.get_power_value(x, n/2)
		if n&1 == 1:
			return x*pow_value*pow_value
		return pow_value*pow_value
	def taking_input_data(self):
		print "Enter x:",
		x = input()
		print "Enter n:",
		n = input()
		print "Enter d:",
		d = input()
		print "Answer:", self.get_power_value(x, n)%d
obj = calculate_power()
obj.taking_input_data()