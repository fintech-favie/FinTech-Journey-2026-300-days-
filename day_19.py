price = 19500
trend_up = True
if price <20000 and trend_up == True:
	print("signal: buy now")
else:
	print("signal:wait ")
	
is_saturday = True
is_sumday = False
if is_saturday or is_sunday:
	print("market is closed")
