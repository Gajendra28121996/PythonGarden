#for- define the respect range.  if-conditional statement. break- used to brak the flow of flow of module if condition satisfied.
#for,if,continue,break,else,elif
for letter in 'Python':
	print 'Current Letter : ',letter

fruits = ['banana','apple','raspbery','tomato','mango']
for fruits in fruits:
	if fruits == 'mango':
		break
	elif fruits =='apple':
		continue
		print(" Continued from here !")
	else:
		print 'Current Fruits : ', fruits	
	
print "And Done !"