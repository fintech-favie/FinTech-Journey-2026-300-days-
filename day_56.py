
print("--- 🛠️ DAY 56: STABILIZING THE LOGIC ---")

# The Core Build
num_a = float(input("Enter value: "))
num_b = float(input("Divide by: "))

# The Safety Gate
if num_b != 0:
    print("Success! Result is:", num_a / num_b)
else:
    print("Error: The divisor cannot be zero.")
