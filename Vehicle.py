class Vehicle:
	def __init__(self,name,model):
		self.name=name
		self.model=model
		# self.color=color
		# self.engine=engine
		# self.milage=milage
	def display(self):
		return "{} {}".format(self.name,self.model)

# blu=Vehicle("Glue",43434)
# print(blu.display())
# print(blu.name)

class Car(Vehicle):
	def __init__(self):
		# Vehicle.display(self)
		# print("Super !!")

	def good(self,name):
		print(name)	
	def pattern(self):
		n = 10
		for idx in range(n-1):
		    print((n-idx) * ' ' + (2*idx+1) * '*')
		for idx in range(n-1, -1, -1):
		    print((n-idx) * ' ' + (2*idx+1) * '*')

	


inhertClass=Car()
inhertClass.good("Gajendra")
# inhertClass.pattern()


		















# 	def Details(self,name):
# 		print(" Your Given details : ")
# 		return "Name : {} ".format(self,name)
# desk=Vehicle("dewd","s","ds","ds","c")
# print(desk.Details("dewd","s","ds","ds","c"))

# def Details(self,name,model,color,engine,milage):
# 		print(" Your Given details : ")
# 		return "Name : {} \nModel: {} \nColor : {}\nEngine : {}\nMilage : {}".format(self,name,model,color,engine,milage)