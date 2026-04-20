import pprint

Social_app = {
    "user_101": {"username": "favie", "posts": 85, "active": True},
    "user_102": {"username": "alex_dev", "posts": 45, "active": False},
    "user_103": {"username": "pro", "posts": 12, "active": True}
}

for id, data in Social_app.items():
    if data["posts"] >= 50 and data["active"] == True:
        data["tier"] = "VIP"
    elif data["posts"] >= 20 or data["active"] == True:
        data["tier"] = "Standard"
    else:
        data["tier"] = "Guest"

pprint.pprint(Social_app)
