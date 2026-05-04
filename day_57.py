# Day 57: Permanent Logic Lock
print("--- ⚙️ DAY 57: LOGIC REINFORCEMENT ---")

# Step 1: Get the data
val_1 = float(input("Enter number: "))
val_2 = float(input("Divide by: "))

# Step 2: Check the gate
if val_2 != 0:
    print("Result:", val_1 / val_2)
else:
    print("Blocked: Zero is not allowed here.")
