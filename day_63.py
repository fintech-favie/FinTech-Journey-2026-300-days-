# Day 63: Perfect Discount Logic
price = float(input("Price: "))
disc = float(input("Discount %: "))
save = (price * disc) / 100
print(f"You save: ₹{save} | Pay: ₹{price - save}")
