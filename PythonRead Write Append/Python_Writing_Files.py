employee_file=open("employees.txt","a")
employee_file.write("\nHarsh - SEO")
employee_file.close()

employee_file=open("employees.txt","r")
print("Your Modified File : \n\n"+employee_file.read())
employee_file.close()