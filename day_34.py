
Company = { 
    "finance": {"lead": "anshika", "target": 50, "status": "active"}, 
    "tech": {"lead": "alex", "target": 30, "status": "hiring"},
    "marketing": {"lead": "rahul", "target": 55}
}

print("--- HIGH VALUE DEPARTMENTS ---")

for dept, details in Company.items():
   
    if details["target"] >= 50:
        print(f"Department : {dept.upper()}")
        print(f"Lead       : {details['lead'].title()}")
        print(f"Target     : {details['target']}LPA")
        print("-" * 15)
