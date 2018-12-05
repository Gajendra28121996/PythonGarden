# " r " is for Read Only Operation
# open("employees.txt","r")

# # " w " is for Write Only Operation
#  open("employes.txt","w")

# # " a " stands for append and  is for Update or Modify the data
#  open("employes.txt","a")

# # " r+ " is for Read and Write both Operation
#  open("employes.txt","r+")
#===================================================================
## w+ means it will create file it it does not Exist
employee_File=open("employee.txt","w+")
employee.write("You Just Used Write Operation to your File")
employee_File.close()