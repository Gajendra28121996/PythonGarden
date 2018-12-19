#The finally block will always be executed, no matter if the try block raises an error or not:

try:
	number=int(input("Enter a number : "))
	print(number)
	1/number
except ZeroDivisionError:
	print("Divided by Zero")
except:
	print("Invalid Input")
finally:
	print("Expect Block finished !")
## Above are some BAD PRACTICES you Should'nt Follow !
print(" \nBetter Practice Results \n")
# For GOOD PRACTICES use predefined exception with - err and print(err)
try:
	number = int(input("Enter a number : "))
	print(number)
	1/number

except ZeroDivisionError as err:
	print(err)
## Python will Show an Error.  Run the Program in Python3
except ValueError:
	print("Invalid Input Please Input Number !")