is_male=True
is_tall=False
if is_male:
	print("You are Male !!")
else:
	print("You are Probably Good !")
##When one or both of value is true use OR
if is_male or is_tall:
	print("You are Male && Tall!!")
else:
	print("You are Probably Good Nor Tall!")
##Mandatory to both to be true
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

if is_male and is_tall:
	print("You are Male and Tall !")
elif is_male and not(is_tall):
	print("You are Male Not Tall!")
elif not(is_male) and is_tall:
	print("you are Not Male and but Tall")
elif not(is_male) and not(is_tall):
	print("You are Not male and Nor Tall")