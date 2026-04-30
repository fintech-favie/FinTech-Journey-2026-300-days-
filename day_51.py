Print("---- Day 51: Profit/Loss Analyzer ----")

# Getting inputs
buy_price = float(input("Enter Purchase Price: "))
sell_price = float(input("Enter Selling Price: "))

# Logic to calculate difference
difference = sell_price - buy_price

print("-" * 30)

if difference > 0:
    print(f"Status: PROFIT! You made: {difference:.2f}")
elif difference < 0:
    print(f"Status: LOSS. You lost: {abs(difference):.2f}")
else:
    print("Status: BREAK-EVEN. No profit, no loss.")

print("-" * 30)


So basically this one is (subtraction one right)