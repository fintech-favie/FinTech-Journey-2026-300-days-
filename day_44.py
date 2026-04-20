import pprint

Social_app = {
    "user_101": {"username": "favie", "posts": 200, "active": True},
    "user_102": {"username": "alex_dev", "posts": 95, "active": True},
    "user_103": {"username": "pro", "posts": 110, "active": False},
    "user_104": {"username": "alpha", "posts": 45, "active": True}
}

for user_id, info in Social_app.items():
    if info["posts"] >= 150 and info["active"]:
        info["account_type"] = "Super_Creator"
    elif info["posts"] >= 80 and info["active"]:
        info["account_type"] = "Rising_Star"
    elif info["posts"] >= 80 or info["active"]:
        info["account_type"] = "Verified_Member"
    else:
        info["account_type"] = "Basic_User"

pprint.pprint(Social_app)
