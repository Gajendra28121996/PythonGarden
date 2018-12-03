####################### String Operation ##############################

## Print Call Function

phase = "Giraffe Gone Mad !"
print(phase)

##Concatination 
print(phase+" Really "+"")

## Boolean Function
print(phase.isupper())

## Upper case Function for 
print(phase.upper())

## Combination of Function with dot operator
print(phase.upper().isupper())

## Length of Character in Phase variable with len() 
print(len(phase))

## Find whose sat(located) on index number of array with variable_name[]
print(phase[0]+phase[9]+phase[15]+"")

## Find Index Fuctions
	## Finding index number
print(phase.index("a"))
	## can use whole string but in result we get the  index number ndex
print(phase.index("Gone"))
	## replace("Target String","Modifiction for the target string")
print(phase.replace("Giraffe","Krishna"))