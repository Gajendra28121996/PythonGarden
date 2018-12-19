def outer():
	x='local var'

	def inner():
		nonlocal x
		x="nonlocal"
		print("inner",x)
	inner()
	print("Outer : ",x)
outer()