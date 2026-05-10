#day : 62
amt = float(input("total cash : "))
spend = float(input("total spent : "))
print(f"left over change : $ { amt % spend}")