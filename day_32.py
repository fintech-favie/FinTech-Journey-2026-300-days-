
Company = { 
    "engineering": { "lead": "anshika", "target": "45lpa" }, 
    "design": { "lead": "alex", "target": "30lpa" } 
}

for dept, info in Company.items():
   
    print(f"department : {dept.title()}")
    print(f"lead name : {info['lead']}")
    print(f"income target : {info['target']}")
    print("-" * 15)
