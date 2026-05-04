
print("--- 📈 DAY 58: PROFIT MARGIN CALC ---")

# 1. Input Data
cost = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

# 2. Combined Logic
profit = selling_price - cost

# 3. The Safety Gate (Practiced from Day 54-57!)
if selling_price != 0:
    margin = (profit / selling_price) * 100
    print("-" * 30)
    print(f"Total Profit: ₹{profit}")
    print(f"Profit Margin: {margin}%")
else:
    print("Error: Selling price cannot be zero.")
