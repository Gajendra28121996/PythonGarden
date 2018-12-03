## return allows return somthing from a function
def cube(num):
	num*num*num
print(cube(3))

#####Above program return NONE because we have'nt used return
## or haven't stored in any variable

def Correct_Cube(num):
	return num*num*num
print(Correct_Cube(3))
result=Correct_Cube(6)
print(result)

##Function for string
def StringManipulation(str):
	x="Ojha"
	return str+x
print(StringManipulation("Gajendra "))