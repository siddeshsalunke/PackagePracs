from vehicles import Engine
from vehicles import Color
from vehicles import Wheels

class AskUser():
	power = Engine()

	def __init__(self):
		pass
	
	def checkUserInput(self):
		colors_obj = Color()
		var = raw_input("What type of Vehicle you need?? Please Enter Car Or Bike: ")
		if var == 'Car':
			showpowercars = self.power.fourWheelerEngine()
			print ("Available Car Options with power " + str(showpowercars) + "Color" +str(colors_obj.printColors()))
		
		if var == 'Bike':
			showpowerbikes = self.power.twoWheelerEngine()
			print ("Available Bike Options with power " + str(showpowerbikes) + "Color" +str(colors_obj.printColors()))
			
choose = AskUser()
choose.checkUserInput()

