
print("---  DAY 53: RATIO & AVERAGING ---")


total_investment = float(input("Enter Total Amount Spent: ₹"))
total_units = float(input("Enter Number of Units bought: "))

if total_units > 0:
    avg_price = total_investment / total_units
    print("-" * 30)
    print(f"Your Average Buying Price: ₹{avg_price}")
else:
    print("-" * 30)
    print("❌ Error: Units must be greater than zero!")
