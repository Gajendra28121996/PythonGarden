## List of number
list_Of_Number=[3,4,6,9,11,13]
friends=["Gajendra","Stan Lee","Repeating","Enstine","Iron Man","Skarlett Jhonson","Repeating","Repeating"]

print(friends)
print(list_Of_Number)

## append() >>> Allows me to append another item to the list
friends.append("Creed")
print(friends) 
##Print the Index of List Element
print(friends.index("Creed"))
## inser(index_num, value_to_be_Inserted) >>> Allows me to inset an item at specified index.
## Function will insert an elemnet in the pecified index and  all list element will be adjusted with respect to the insertion
friends.insert(2,"Stephen Hawkings")
print(friends)
## remove( element to be removed ) 
friends.remove("Enstine")
print(friends)
## pop removes the last elemnt from the list
friends.pop()
print(friends)
##Count How many timmes the word occur in the list
print(friends.count("Repeating"))
## Sort() >>> sort in alphabetical order
friends.sort()
print(friends)
##Reverse the List
friends.reverse()
print(friends)
## hold the Copy of the list in another variable
strange_friend=friends.copy()
print(strange_friend)

## clear() >>> Reset the list or cleas all element from the list
friends.clear()
print(friends)
