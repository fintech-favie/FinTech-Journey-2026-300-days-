Company = {
    "finance": {
        "lead": "anshika",
        "target": "50lpa",
        "status": "active"
    },
    "tech": {
        "lead": "alex",
        "target": "45lpa",
        "status": "hiring"
    }
}

for dept, details in Company.items():
    print(f"--- {dept.upper()} REPORT ---")
    print(f"Manager   : {details['lead'].title()}")
    print(f"Objective : {details['target']}")
    print(f"Status    : {details['status']}")
    print("*" * 20)
