# https://docs.python.org/3/library/exceptions.html#Warning
# above link have reference of all builtin exception.
print("\nhttps://docs.python.org/3/library/exceptions.html#Warning\n")
print("above link have reference of all builtin exception python have.\n")
try:
	# value=10/0
	number=int(input("Enter a number : "))
	print(number)
except ZeroDivisionError:
	print("Divided by Zero")
except:
	print("Invalid Input")
## Above are some BAD PRACTICES you Should'nt Follow !
 
# For GOOD PRACTICES use predefined exception with - err and print(err)
try:
	# value=10/0
	number = int(input("Enter a number : "))
	print(number)
except ZeroDivisionError as err:
	print(err)
## Python will Show an Error.  Run the Program in Python3
except ValueError:
	print("Invalid Input Please Input Number !")

try:
   file = open("demo_file", "r")
   file.write("This is my demo_file for exception handling!!")
except IOError as err:
   print(err)
else:
   print("Written content in the file successfully")