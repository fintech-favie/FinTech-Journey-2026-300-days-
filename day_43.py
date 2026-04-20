import pprint

Social_app = {
    "user_101": {"username": "favie", "posts": 150, "active": True},
    "user_102": {"username": "alex_dev", "posts": 85, "active": False},
    "user_103": {"username": "pro", "posts": 60, "active": True},
    "user_104": {"username": "newbie", "posts": 15, "active": True}
}

for user_id, info in Social_app.items():
    if info["posts"] >= 100 and info["active"]:
        info["access_level"] = "Premium_Plus"
    elif info["posts"] >= 50 and info["active"]:
        info["access_level"] = "Premium"
    elif info["posts"] >= 50 or info["active"]:
        info["access_level"] = "Standard"
    else:
        info["access_level"] = "Restricted"

pprint.pprint(Social_app)
