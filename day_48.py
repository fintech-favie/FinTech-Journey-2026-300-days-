
print("--- 🚀 TASK MANAGER ENGINE ---")
task_name = input("Enter your current project name: ")
hours_spent = float(input(f"How many hours did you work on {task_name}? "))
if hours_spent >= 5:
    status = "DEEP WORK SESSION"
    efficiency = "High"
elif hours_spent > 0:
    status = "QUICK TASK"
    efficiency = "Moderate"
else:
    status = "INVALID ENTRY"
    efficiency = "N/A"

print("-" * 30)
print(f"Project: {task_name}")
print(f"Status: {status}")
print(f"Efficiency Level: {efficiency}")
