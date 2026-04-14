Company = {
    "finance": {"lead": "anshika", "target": 50},
    "tech": {"lead": "alex", "target": 45},
    "marketing": {"lead": "rahul", "target": 30}
}
total_target = 0
for dept , details in Company.items( ):
	total_target = total_target + details["target"]
	print(f"Added {dept}: + {details['target']}LPA")
	print("-" * 20)
	print(f"Total Company target :{total_target}LPA")
