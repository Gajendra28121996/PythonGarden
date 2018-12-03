##User Balance
## Program that Verifies the PIN and allow access to service function


user1_bal=10000

def welcome():
	print("Welcome To Fake Banking")
	print("Pin is 1234")
	verification_and_packeting()

def banking():
	print("Select Services : ")
	print("1. Withdrawl ")
	print("2. Deposit ")
	# print("3. Money Transfer")
	# print("4. ATM Card Information")
	# print("5. Balance Inquiries")
	selection=input("Enter your Choice : ")

	if selection=="1":
		Withdrawl()
	elif selection=="2":
		Deposit()
	elif selection=="3":
		Money_Transfer()
	elif selection=="4":
		ATM_Card_Information()
	elif selection=="5":
		Balance_Inquiries()
	else:
		print("Invalid Input ! ")
### Widthdrawl Function
def Withdrawl():
	print("1. Saving Account")
	print("2. Current Account")
	acc_type=input("Select the Account type You have :")
	if acc_type=="1":
		Withdrawl_amt=input("Amount : ")
		done=input("Conform : ")
		if done=="y":
			bal=float(user1_bal)-float(Withdrawl_amt)
			print("Transfer Amount : "+str(Withdrawl_amt))
			print("Available balance : "+str(bal))
		
	elif acc_type=="2":
		Withdrawl_amt=input("Amount : ")
		done=input("Conform : ")
		if done=="y":
			bal=float(user1_bal)-float(Withdrawl_amt)
			print("Transfer Amount : "+str(Withdrawl_amt))
			print("Available balance : "+str(bal))
	else:
		print("Invalid Input ! ")

def Deposit():
	
	print("1. SBI to SBI")
	print("2. SBI to Another")
	Deposit_type=input("Select your transfer type : ")
	if Deposit_type=="1":
		Receiver_acc=input("Account no : ")
		isfc=input("ISFC Code : ")
		Transf_amt=float(input("Amount : "))
		done=input("Conform : ")
		if done=="y":
			bal=float(user1_bal)+float(Transf_amt)
			print("Receiver Acc No.: "+str(Receiver_acc))
			print("Transfer Amount : "+str(Transf_amt))
			print("Available balance : "+str(bal))
			
			


	if Deposit_type=="2":
		bnk_name=input(" Bank Name :")
		bnk_brch=input(" Bank Branch :")
		bnk_brch_code=input(" Bank Branch Code :")
		Receiver_acc=input("Account no : ")
		isfc=input("ISFC Code : ")
		Transf_amt=int(input("Amount : "))
		done=input("y")
		if done=="y":
			bal=float(user1_bal)+float(Transf_amt)
			print("Receiver Acc No.: "+str(Receiver_acc))
			print("Transfer Amount : "+str(Transf_amt))
			print("Available balance : "+str(bal))
			
##Verification of User
def verification_and_packeting():
	user_pin="1234"
	user_input=""
	guess_count=0
	guess_limit=2
	out_of_guess=False
	while user_input!= user_pin and not(out_of_guess):
		if guess_count<=guess_limit:
			user_input=input("Enter PIN : ")
			guess_count+=1
		else:
			out_of_guess=True
	if out_of_guess:
		print("You are Restricted to Transact ! ")
	else:
		print("PIN was Correct !")
		banking()

## Initial Call to Intial Function'...
welcome()
