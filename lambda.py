
#lambda used to store variable with passing into function simultaneously
var_name=lambda a,b,c:a+b+c
# A lambda function can take any number of arguments, 
ip_mul_var=lambda c,d:c*d
# but can only have one expression.
print(var_name(5,6,7))

m=input("1st number : ")
x=input("2nd number : ")
print(ip_mul_var(m,x))

x=True

if x:
	print("T")
else:
	print("f")