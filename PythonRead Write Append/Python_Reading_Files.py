# Suppose we have a text file
# We are in same Directory so will directly name our file

# " r " is for Read Only Operation
# open("employees.txt","r")

# # " w " is for Write Only Operation
#  open("employes.txt","w")

# # " a " stands for append and  is for Update or Modify the data
#  open("employes.txt","a")

# # " r+ " is for Read and Write both Operation
#  open("employes.txt","r+")
#===================================================================
#employee_variable is used to store text file content in it
employee_file=open("employees.txt","r")
# if have read permission then we verify it by readable()
print(employee_file.readable())
# Now Lets Read the File
print(employee_file.read())
print("----------------------------------")
#Just like open we have to close the file too
employee_file.close()


# want to read file LINE BY LINE here it goes
employee_file=open("employees.txt","r")
print(employee_file.readable())
print(employee_file.readline())
print("----------------------------------")
employee_file.close()

# >>Look if we have used read() method then we cant get the result of
#   readline function.
employee_file=open("employees.txt","r")
print(employee_file.read())
print(employee_file.readline())
print("----------------------------------")
employee_file.close()
# >>Another thing If you have used readline() 
#   then read() will start read operation from next line
employee_file=open("employees.txt","r")
print(employee_file.readline())
print(employee_file.read())
print("----------------------------------")
employee_file.close()

# Better method of readline() is readlines() to print all lines
employee_file=open("employees.txt","r")
# This will put all lines in list and display postfixed by "\n" to represent new line
print(employee_file.readlines())
print("----------------------------------")
employee_file.close()

# Listing File Content using For Loop
employee_file=open("employees.txt","r")
for List_element in employee_file.readlines():
	print(List_element)
employee_file.close()

