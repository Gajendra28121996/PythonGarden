## 2D Lists
number_grid=[

			[1,2,3,4,5,6,7,8,9],# <<Row 0
			[2,5,2,1,5,3,8,8,9],# <<Row 1
			[3,2,3,4,5,6,7,8,9],# <<Row 2
			[4,5,2,1,5,3,8,8,9],# <<Row 3
#	    	 ^^^^^^^^^^^^^^^^^
#	    	 ^^^^^^^^^^^^^^^^^    
    ##Column[0,1,2,3,4,5,6,7,8]
]
##print(number_grid([ROW][COLUMN]))
print(number_grid[3][5])
### Print the 2 D List
for row in number_grid:
	for column in row:
		print(column)