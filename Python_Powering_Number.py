##Exponent Function take a number and raise it to a power example : 2^3 =2*2*2 = 8

def raise_to_power(base_num, pow_num):
	result=1
	for index in range(pow_num):
		result=result*base_num
	return result

print(raise_to_power(5,3))
