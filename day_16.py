current_price = 6500
buy_limit = 5800
if current_price  <= buy_limit :
	print("market status : price is low ")
	print("action : buy now")
else:
	print("market status : price is high")
	print("action: wait ")
	
live_price = int("67890")
target_price = 6000
if live_price <=  target_price :
	print(f"price is {live_price} . buy now")
else:
	print(f"price is {live_price}.its to high wait !!")
	