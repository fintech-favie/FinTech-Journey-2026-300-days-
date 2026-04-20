import pprint

Social_app = {
    "user_101": {"username": "favie", "posts": 120, "active": True},
    "user_102": {"username": "alex_dev", "posts": 55, "active": True},
    "user_103": {"username": "pro", "posts": 30, "active": False},
    "user_104": {"username": "tester", "posts": 5, "active": True}
}

for user_id, info in Social_app.items():
    if info["posts"] > 100 and info["active"]:
        info["status"] = "Elite"
    elif info["posts"] >= 50 and info["active"]:
        info["status"] = "Priority"
    elif info["posts"] >= 20 or info["active"]:
        info["status"] = "Active_User"
    else:
        info["status"] = "Inactive"

pprint.pprint(Social_app)
