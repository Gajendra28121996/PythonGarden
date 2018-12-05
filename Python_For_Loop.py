## This For Loop will print out each letter going through the string "Girrafe"

for letter in "Girrafe" :
	 ## For each Letter in Girrafe i want to do something
	 ## So What it does at first iteration letter will store "G" on next iteration it will store "i " and so on and print
	 print(letter)

friends_array=["Nikita","Krishna","Monika"]
print("---------------------------------------------")

## This will print 0 to 9 but not the 10.
for index in range(10):
	pass
	print(index)
	
print("-----------------------------------------------")
## Little bit nested
for index in range(9):
	if index==0:
		print("Powering Board")
	elif index==1:
		print("Booting")
	elif index==2:
		print("Initiated System Apps")
	else:
		print("Security Checks!")
print("-----------------------------------------------")
## This will print 3 to 9 NOT 10
for index in range(3,10):
	pass
	print(index)

print("-----------------------------------------------")
for index in range(len(friends_array)):
	pass
	print(friends_array[index])