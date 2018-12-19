#The assert keyword is used when debugging code.
#An if statement will not raise an exception when the condition is false.
#Assertion will raise an assertion error when the condition is false.
#An assertion exception will stop the program unless the exception is handled by a try-except block.
# def Like(choice):
# 	assert (choice<=0), "You Liked it !"

# print Like(1)

# # if contition returns true, then nothing happens:
# assert x=="Gajendra Ojha","Goal"

# # if condition returns false then Assertion Error Raised
# assert x=="Good Bye"
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print KelvinToFahrenheit(273)
print int(KelvinToFahrenheit(505.78))
print KelvinToFahrenheit(-5)