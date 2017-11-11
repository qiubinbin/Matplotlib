from random import randint
class Die():
	"""表示筛子的类"""
	def __init__(self,num_sides=6):
		"""筛子六面"""
		self.num_sides=num_sides
	def roll(self):
		"""返回随机的一个面"""
		return randint(1,self.num_sides)