# " r " is for Read Only Operation
# open("employees.txt","r")

# # " w " is for Write Only Operation
#  open("employes.txt","w")

# # " a " stands for append and  is for Update or Modify the data
#  open("employes.txt","a")

# # " r+ " is for Read and Write both Operation
#  open("employes.txt","r+")
#===================================================================
## w+  here + (Plus Sign )means it will create file that does not Exist
employee_File=open("employee.txt","w+")
employee_File.write("You Just Used Write Operation to your File")
employee_File.close()

file_name="employee.txt"
employee_File=open(file_name,"r")
print("Your "+file_name+" Contains : \n\n"+employee_File.read())
employee_File.close()