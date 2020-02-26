class Car():

	def __init__(self, name):
		self.name = name
		self.maxGear = 4
		self.actualGear = 0
		self.maxSpeed = 200
		self.actualSpeed = 0
		self.speedTreshold = 50
		self.speedHistory = []

	def info(self):
		print("My name is: {} /n"
			"actualGear :{} /n"
			"actualSpeed :{} /n".format(self.name, self.actualGear, self.actualSpeed))

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


	def gearRequiredAtActualSpeed(self):
		return self.actualSpeed // self.speedTreshold + 1

	def changeGearWhenTresholdReached(self):
		if self.actualGear < self.gearRequiredAtActualSpeed():
			self.gearUp()
			print("Gearing up")
		if self.actualGear > self.gearRequiredAtActualSpeed():
			self.gearDown()
			print("Gearing down")


	def increaseSpeed(self):
		if self.actualSpeed < (self.maxSpeed - 9):
			self.actualSpeed += 10
		else:
			print("You are at max speed!!! You can not increase speed")

	def decreaseSpeed(self):
		if self.actualSpeed > 10:
			self.actualSpeed -= 10
		print("You are at 0 speed!!! You can not slow down")


	def hitGas(self):
		self.increaseSpeed()
		self.changeGearWhenTresholdReached()
		self.info()

	def hitBrake(self):
		self.decreaseSpeed()
		self.changeGearWhenTresholdReached()
		self.info()

car1 = Car("car1")
car1.info()
for item in range(22):
	car1.hitGas()
