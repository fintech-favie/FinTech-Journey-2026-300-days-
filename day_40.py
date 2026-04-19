import pprint

Social_app = {
    "user_101": {"username": "favie", "posts": 85},
    "user_102": {"username": "alex_dev", "posts": 45},
    "user_103": {"username": "pro", "posts": 12}
}

for id, data in Social_app.items():
    # Tier 1: Gold
    if data["posts"] >= 80:
        data["rank"] = "Gold"
    # Tier 2: Silver (Checks this only if Tier 1 fails)
    elif data["posts"] >= 40:
        data["rank"] = "Silver"
    # Tier 3: Bronze (The fallback)
    else:
        data["rank"] = "Bronze"

pprint.pprint(Social_app)
