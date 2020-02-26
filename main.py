class Car():

	def __init__(self, name):
		self.name = name
		self.maxGear = 4
		self.actualGear = 0
		self.topSpeed = 200
		self.actualSpeed = 0


	def info(self):
		print("My name is: " + self.name)

	def gearUp(self):
		if self.actualGear <= self.maxGear:
			self.actualGear += 1
			print("Actual gear: {}".format(self.actualGear))
		else:
			print("You can not gear up. You are at max gear: {}".format(self.actualGear))

	def gearDown(self):
		if self.actualGear > 0:
			self.actualGear -= 1
			print("Actual gear: {}".format(self.actualGear))
		else:
			print("You can not gear down. You are actually at neutral {}".format(self.actualGear))

	self.

car1 = Car("car1")
car1.info()
car1.gearDown()
car1.gearUp()
car1.gearUp()
car1.gearUp()
car1.gearUp()
car1.gearUp()
car1.gearUp()