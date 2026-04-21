import pprint

Social_app = {
    "user_101": {"username": "favie", "posts": 250, "active": True},
    "user_102": {"username": "alex_dev", "posts": 90, "active": True},
    "user_103": {"username": "pro", "posts": 150, "active": False},
    "user_104": {"username": "member_x", "posts": 20, "active": True}
}
vip_count = 0
standard_count = 0 
for id, info in Social_app.items( ):
	if info["posts"] >= 100 and info["active"]:
		info["tier"] = "vip"
		vip_count += 1
	else:
			info["tier"] = "standard"
			standard_count += 1
			print("database update completed")
			pprint.pprint(Social_app)
			print("-" * 30)
			print(f"total vip users:{vip_count}")
			print(f"total standard users:{standard_count}")
			 

		
	    import pprint

Social_app = {
    "user_101": {"username": "favie", "posts": 250, "active": True},
    "user_102": {"username": "alex_dev", "posts": 90, "active": True},
    "user_103": {"username": "pro", "posts": 150, "active": False},
    "user_104": {"username": "member_x", "posts": 20, "active": True}
}
vip_count = 0
standard_count = 0 
for id, info in Social_app.items( ):
	if info["posts"] >= 100 and info["active"]:
		info["tier"] = "vip"
		vip_count += 1
	else:
			info["tier"] = "standard"
			standard_count += 1
			print("database update completed")
			pprint.pprint(Social_app)
			print("-" * 30)
			print(f"total vip users:{vip_count}")
			print(f"total standard users:{standard_count}")
			 

		
	    