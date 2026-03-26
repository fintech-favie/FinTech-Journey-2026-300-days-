is_verified = True
balance = 10000
withdraw_amount = 2000
if is_verified == True :
	print("verification success")
	if balance >= withdraw_amount :
		print("transaction approved")
		balance = balance - withdraw_amount
		print("new balance:,balance")
else:
	print("transaction declined")
	
is_verified = True 
balance = 10000
withdraw_amt = 2000
if is_verified == True :
	print("verification success")
	if balance >= withdraw_amount:
		print("transaction approved")
		balance = balance - withdraw_amt
		print("new balance:,balance")
else:
	print("verification denied")
	