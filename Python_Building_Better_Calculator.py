def Calculator():
	number_1=float(input("Enter first Number : "))
	number_2=float(input("Enter Second Numeber :"))
	Operator=input("What Operation to be Performed :")

	if Operator=="+":
		print(number_1 + number_2)
	elif Operator=="-":
		print(number_1 - number_2)
	elif Operator=="*":
		print(number_1 * number_2)
	elif Operator=="/":
		print(number_1/number_2)
	else:
		print("Undefined Operator !!!!")
	print("------------------------------")
	Start()

def Start():
	Continue=input("Start again !!")
	while Continue!="r":
		print("Succesfully Said Bye to Caluclator")
		Calculator()

print("Welcome to Better Calculator ")
Start()