# " r " is for Read Only Operation
# open("employees.txt","r")

# # " w " is for Write Only Operation
#  open("employes.txt","w")

# # " a " stands for append and  is for Update or Modify the data
#  open("employes.txt","a")

# # " r+ " is for Read and Write both Operation
#  open("employes.txt","r+")
#===================================================================

employee_file=open("employees.txt","a")
employee_file.write("\nHarsh - SEO")
employee_file.close()

employee_file=open("employees.txt","r")
print("Your Modified File : \n\n" + employee_file.read())
employee_file.close()